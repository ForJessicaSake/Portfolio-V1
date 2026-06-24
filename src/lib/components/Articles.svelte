<script lang="ts">
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { articles } from '$lib/data/articles';
</script>

<section id="writing" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-2" style="--child-i: 0">writing</p>
		<p class="reveal-child mb-6 max-w-[520px] text-[13px] leading-[1.65] text-ink-mid" style="--child-i: 1">
			Technical writing across Smashing Magazine, Frontend Mentor, OpenReplay, and Turing — practical
			guides on React, TypeScript, and modern web development.
		</p>

		<ul class="flex flex-col gap-3">
			{#each articles as article, i}
				<li class="reveal-child" style="--child-i: {i + 2}">
					<a
						href={article.url}
						class="article-item group block rounded-[6px] border border-rule bg-card p-5"
						target="_blank"
						rel="noopener noreferrer"
					>
						<div class="mb-2 flex items-start justify-between gap-4">
							<div>
								<p class="mb-1 text-[11px] tracking-wide text-accent uppercase">
									{article.publication}
								</p>
								<h3
									class="text-[15px] font-medium text-ink transition-colors duration-150 group-hover:text-accent-warm"
								>
									{article.title}
								</h3>
							</div>
							<span
								class="shrink-0 pt-1 text-[14px] text-ink-faint transition-colors duration-150 group-hover:text-accent"
								aria-hidden="true"
							>
								↗
							</span>
						</div>
						<p class="mb-2 text-[13px] leading-[1.65] text-ink-mid">{article.description}</p>
						<p class="text-[11px] text-ink-faint">{article.date}</p>
					</a>
				</li>
			{/each}
		</ul>
	</div>
</section>
