<script lang="ts">
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { aboutBio, aboutHighlights } from '$lib/data/about';
</script>

<section id="about" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-5" style="--child-i: 0">about</p>

		<div class="reveal-child mb-8 space-y-4" style="--child-i: 1">
			{#each aboutBio as paragraph}
				<p class="text-[14px] leading-[1.75] text-ink-mid">{paragraph}</p>
			{/each}
		</div>

		<ul class="grid grid-cols-1 gap-3 sm:grid-cols-2">
			{#each aboutHighlights as item, i}
				<li
					class="reveal-child rounded-[6px] border border-rule bg-card p-4"
					style="--child-i: {i + 2}"
				>
					<p class="mb-1.5 text-[13px] font-medium text-ink">{item.title}</p>
					<p class="text-[12px] leading-[1.65] text-ink-mid">{item.body}</p>
				</li>
			{/each}
		</ul>
	</div>
</section>
