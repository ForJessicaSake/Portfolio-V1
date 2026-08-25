#!/usr/bin/env python3
"""Download the Peerless ERM PDF-viewer pages and compile them into Markdown.

The viewer at https://riskassesment.bepeerless.co/pdf-viewer/ does not expose a
.pdf file. It serves rasterised pages as PNG images:

    /static/pdf_pages/page_001.png ... page_047.png

This script:
  1. Reads the viewer HTML to learn the page count
  2. Downloads every page image
  3. OCRs each page (macOS Vision by default, Tesseract as fallback)
  4. Writes a single Markdown file

Usage:
    python3 scripts/extract_erm_pdf.py
    python3 scripts/extract_erm_pdf.py -o erm-framework.md
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

VIEWER_URL = "https://riskassesment.bepeerless.co/pdf-viewer/"
PAGE_IMAGE_URL = "https://riskassesment.bepeerless.co/static/pdf_pages/page_{page:03d}.png"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

FOOTER_PATTERNS = [
    re.compile(r"^confidential\s*[–\-]\s*peerless", re.I),
    re.compile(r"^doc\s*id\s*:", re.I),
    re.compile(r"^sealed\s*:", re.I),
    re.compile(r"^page\s+\d+\s+of\s+\d+$", re.I),
    re.compile(r"^lexworth\s+legal", re.I),
    re.compile(r"^dano\s+\d+", re.I),
]

SWIFT_OCR = r"""
import Vision
import AppKit
import Foundation

guard CommandLine.arguments.count >= 2 else {
    fputs("usage: ocr_page <image-path>\n", stderr)
    exit(1)
}

let path = CommandLine.arguments[1]
let url = URL(fileURLWithPath: path)
guard let image = NSImage(contentsOf: url),
      let tiff = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiff),
      let cgImage = bitmap.cgImage else {
    fputs("failed to load image: \(path)\n", stderr)
    exit(1)
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["en-US"]

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
do {
    try handler.perform([request])
} catch {
    fputs("ocr failed: \(error)\n", stderr)
    exit(1)
}

struct Box: Codable {
    let text: String
    let x: Double
    let y: Double
    let w: Double
    let h: Double
    let confidence: Double
}

let observations = request.results ?? []
let boxes: [Box] = observations.compactMap { obs in
    guard let candidate = obs.topCandidates(1).first else { return nil }
    let r = obs.boundingBox
    return Box(
        text: candidate.string,
        x: r.origin.x,
        y: r.origin.y,
        w: r.size.width,
        h: r.size.height,
        confidence: Double(candidate.confidence)
    )
}

let encoder = JSONEncoder()
let data = try! encoder.encode(boxes)
FileHandle.standardOutput.write(data)
FileHandle.standardOutput.write(Data("\n".utf8))
"""


@dataclass
class Box:
    text: str
    x: float
    y: float
    w: float
    h: float
    confidence: float

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    @property
    def right(self) -> float:
        return self.x + self.w


class TotalPagesParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.total: int | None = None

    def handle_data(self, data: str) -> None:
        if self.total is not None:
            return
        match = re.search(r"const\s+totalPages\s*=\s*(\d+)", data)
        if match:
            self.total = int(match.group(1))


def request_bytes(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def detect_total_pages(viewer_url: str) -> int:
    html = request_bytes(viewer_url).decode("utf-8", errors="replace")
    parser = TotalPagesParser()
    parser.feed(html)
    if parser.total:
        return parser.total
    match = re.search(r"Page\s+\d+\s*/\s*(\d+)", html)
    if match:
        return int(match.group(1))
    raise RuntimeError(f"Could not detect page count from {viewer_url}")


def download_pages(total: int, cache_dir: Path) -> list[Path]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for page in range(1, total + 1):
        dest = cache_dir / f"page_{page:03d}.png"
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  [{page:02d}/{total}] cached {dest.name}")
        else:
            url = PAGE_IMAGE_URL.format(page=page)
            print(f"  [{page:02d}/{total}] downloading {url}")
            dest.write_bytes(request_bytes(url))
        paths.append(dest)
    return paths


def compile_vision_ocr(cache_dir: Path) -> Path:
    source = cache_dir / "ocr_page.swift"
    binary = cache_dir / "ocr_page"
    source.write_text(SWIFT_OCR, encoding="utf-8")
    if binary.exists() and binary.stat().st_mtime >= source.stat().st_mtime:
        return binary
    print("Compiling macOS Vision OCR helper...")
    subprocess.run(
        ["swiftc", "-O", "-o", str(binary), str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    return binary


def ocr_with_vision(binary: Path, image: Path) -> list[Box]:
    result = subprocess.run(
        [str(binary), str(image)],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout or "[]")
    return [
        Box(
            text=item["text"].strip(),
            x=float(item["x"]),
            y=float(item["y"]),
            w=float(item["w"]),
            h=float(item["h"]),
            confidence=float(item["confidence"]),
        )
        for item in payload
        if item.get("text", "").strip()
    ]


def ocr_with_tesseract(image: Path) -> list[Box]:
    try:
        from PIL import Image
        import pytesseract
    except ImportError as exc:
        raise RuntimeError(
            "Install pytesseract and pillow, or run on macOS with Swift/Vision."
        ) from exc

    data = pytesseract.image_to_data(Image.open(image), output_type=pytesseract.Output.DICT)
    width = max(data["width"][i] + data["left"][i] for i in range(len(data["text"]))) or 1
    height = max(data["height"][i] + data["top"][i] for i in range(len(data["text"]))) or 1
    boxes: list[Box] = []
    for i, text in enumerate(data["text"]):
        text = text.strip()
        if not text:
            continue
        conf = float(data["conf"][i])
        if conf < 0:
            continue
        top = data["top"][i]
        h = data["height"][i]
        boxes.append(
            Box(
                text=text,
                x=data["left"][i] / width,
                # Vision uses a bottom-left origin; match that here.
                y=1.0 - ((top + h) / height),
                w=data["width"][i] / width,
                h=h / height,
                confidence=max(conf / 100.0, 0.0),
            )
        )
    return boxes


def is_footer(text: str) -> bool:
    compact = re.sub(r"\s+", " ", text).strip()
    return any(pattern.search(compact) for pattern in FOOTER_PATTERNS)


def usable_boxes(boxes: Iterable[Box]) -> list[Box]:
    kept: list[Box] = []
    for box in boxes:
        if box.y < 0.08:
            continue
        if box.confidence < 0.45:
            continue
        if is_footer(box.text):
            continue
        kept.append(box)
    return kept


def group_lines(boxes: list[Box], y_tol: float = 0.012) -> list[list[Box]]:
    items = sorted(boxes, key=lambda box: -box.cy)
    lines: list[list[Box]] = []
    for box in items:
        if lines:
            current = lines[-1]
            current_cy = sum(b.cy for b in current) / len(current)
            if abs(current_cy - box.cy) <= max(y_tol, box.h * 0.6):
                current.append(box)
                continue
        lines.append([box])
    for line in lines:
        line.sort(key=lambda box: box.x)
    return lines


def line_cells(boxes: list[Box], gap: float = 0.035) -> list[str]:
    cells: list[list[Box]] = [[boxes[0]]]
    for box in boxes[1:]:
        prev = cells[-1][-1]
        if box.x - prev.right > gap:
            cells.append([box])
        else:
            cells[-1].append(box)
    return [" ".join(part.text for part in cell).strip() for cell in cells]


def is_heading(text: str, boxes: list[Box]) -> bool:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact or len(compact) > 80:
        return False
    avg_h = sum(box.h for box in boxes) / len(boxes)
    letters = re.sub(r"[^A-Za-z]", "", compact)
    if letters and letters == letters.upper() and len(compact.split()) <= 10:
        return True
    if re.match(r"^\d+(\.\d+)*\.?\s+[A-Z]", compact) and avg_h >= 0.015:
        return True
    if compact.lower() in {
        "about",
        "table of contents",
        "appendix",
        "change control",
        "approval & sign-off",
        "document control sheet",
    }:
        return True
    return False


def heading_level(text: str) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if compact.isupper() and len(compact.split()) >= 6:
        return "#"
    if re.match(r"^\d+\.\s+", compact):
        return "##"
    if re.match(r"^appendix\s+\d+", compact, re.I):
        return "##"
    return "###"


def md_escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def emit_table(rows: list[list[str]]) -> list[str]:
    width = max(len(row) for row in rows)
    normalised = [row + [""] * (width - len(row)) for row in rows]
    header, *body = normalised
    # Key/value sheets often have no header row. Use the first row as header
    # when every cell looks like a label, otherwise synthesise columns.
    looks_like_header = all(
        cell and not cell.endswith(".") and len(cell.split()) <= 6 for cell in header if cell
    )
    if not looks_like_header:
        header = [f"Col {i}" for i in range(1, width + 1)]
        body = normalised
    lines = [
        "| " + " | ".join(md_escape_cell(cell) for cell in header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(md_escape_cell(cell) for cell in row) + " |")
    return lines


def page_to_markdown(boxes: list[Box]) -> str:
    lines = group_lines(usable_boxes(boxes))
    if not lines:
        return "_No extractable text on this page._"

    rendered: list[str] = []
    table_rows: list[list[str]] = []

    def flush_table() -> None:
        nonlocal table_rows
        if table_rows:
            rendered.extend(emit_table(table_rows))
            rendered.append("")
            table_rows = []

    for boxes_in_line in lines:
        cells = [cell for cell in line_cells(boxes_in_line) if cell]
        if not cells:
            continue
        text = " ".join(cells)
        if is_footer(text):
            continue

        is_table_line = len(cells) >= 2
        if is_table_line:
            table_rows.append(cells)
            continue

        flush_table()
        if is_heading(text, boxes_in_line):
            rendered.append(f"{heading_level(text)} {text}")
            rendered.append("")
        else:
            rendered.append(text)

    flush_table()
    return "\n".join(rendered).strip() + "\n"


def compile_markdown(pages: list[tuple[int, str]], source_url: str) -> str:
    parts = [
        "# Enterprise Risk Management Policy and Framework",
        "",
        "Peerless Software Global Services Limited",
        "",
        f"_Extracted from [{source_url}]({source_url})_",
        "",
    ]
    for page_no, body in pages:
        parts.append(f"<!-- page {page_no} -->")
        parts.append(f"## Page {page_no}")
        parts.append("")
        parts.append(body.rstrip())
        parts.append("")
        parts.append("---")
        parts.append("")
    while parts and parts[-1] in {"", "---"}:
        parts.pop()
    parts.append("")
    return "\n".join(parts)


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--viewer-url", default=VIEWER_URL)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=root / "output" / "erm-framework.md",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=root / ".cache" / "pdf_pages",
    )
    parser.add_argument(
        "--backend",
        choices=("auto", "vision", "tesseract"),
        default="auto",
    )
    return parser.parse_args()


def choose_backend(preferred: str, cache_dir: Path) -> tuple[str, Path | None]:
    if preferred in {"auto", "vision"}:
        if sys.platform == "darwin" and shutil.which("swiftc"):
            return "vision", compile_vision_ocr(cache_dir)
        if preferred == "vision":
            raise RuntimeError("macOS Vision OCR requires macOS and the Swift compiler.")
    if shutil.which("tesseract"):
        return "tesseract", None
    raise RuntimeError(
        "No OCR backend available. On macOS install Xcode CLT (swiftc), "
        "or install Tesseract plus pytesseract and Pillow."
    )


def main() -> int:
    args = parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Reading viewer: {args.viewer_url}")
    total = detect_total_pages(args.viewer_url)
    print(f"Found {total} pages")

    print("Downloading page images...")
    images = download_pages(total, args.cache_dir)

    backend, vision_binary = choose_backend(args.backend, args.cache_dir)
    print(f"OCR backend: {backend}")

    pages: list[tuple[int, str]] = []
    for index, image in enumerate(images, start=1):
        print(f"  OCR {index:02d}/{total} {image.name}")
        if backend == "vision":
            assert vision_binary is not None
            boxes = ocr_with_vision(vision_binary, image)
        else:
            boxes = ocr_with_tesseract(image)
        pages.append((index, page_to_markdown(boxes)))

    markdown = compile_markdown(pages, args.viewer_url)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"Wrote {args.output} ({len(markdown):,} characters)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except urllib.error.URLError as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        print(f"Command failed: {exc.cmd}\n{detail}", file=sys.stderr)
        raise SystemExit(1)
