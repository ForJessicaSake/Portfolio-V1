<script lang="ts">
	import { onMount } from 'svelte';

	let mouseX = $state(0);
	let mouseY = $state(0);
	let ringX = $state(0);
	let ringY = $state(0);
	let hovering = $state(false);
	let clicking = $state(false);
	let visible = $state(false);

	const LERP = 0.12;
	const HOVER_SELECTOR =
		'a, button, [role="button"], [role="link"], .proj-card, .work-row, .contact-item, .article-item';

	onMount(() => {
		const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

		if (prefersReducedMotion || isTouchDevice) {
			return;
		}

		document.body.classList.add('has-custom-cursor');
		visible = true;

		let rafId = 0;

		const tick = () => {
			ringX += (mouseX - ringX) * LERP;
			ringY += (mouseY - ringY) * LERP;
			rafId = requestAnimationFrame(tick);
		};

		rafId = requestAnimationFrame(tick);

		const onMove = (e: MouseEvent) => {
			mouseX = e.clientX;
			mouseY = e.clientY;
		};

		const onOver = (e: MouseEvent) => {
			const target = e.target as HTMLElement;
			hovering = !!target.closest(HOVER_SELECTOR);
		};

		const onDown = () => {
			clicking = true;
		};

		const onUp = () => {
			clicking = false;
		};

		window.addEventListener('mousemove', onMove);
		document.addEventListener('mouseover', onOver);
		window.addEventListener('mousedown', onDown);
		window.addEventListener('mouseup', onUp);

		return () => {
			document.body.classList.remove('has-custom-cursor');
			cancelAnimationFrame(rafId);
			window.removeEventListener('mousemove', onMove);
			document.removeEventListener('mouseover', onOver);
			window.removeEventListener('mousedown', onDown);
			window.removeEventListener('mouseup', onUp);
		};
	});
</script>

{#if visible}
	<div
		class="cursor-ring"
		class:is-hover={hovering}
		class:is-click={clicking}
		style="transform: translate({ringX}px, {ringY}px) translate(-50%, -50%){clicking
			? ' scaleX(0.8) scaleY(1.2)'
			: ''};"
		aria-hidden="true"
	></div>
	<div
		class="cursor-dot"
		class:is-hover={hovering}
		style="transform: translate({mouseX}px, {mouseY}px) translate(-50%, -50%);"
		aria-hidden="true"
	></div>
{/if}
