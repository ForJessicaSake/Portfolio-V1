<script lang="ts">
	import { onMount } from 'svelte';
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { stackCategories } from '$lib/data/stack';

	let cascade = $state(false);

	onMount(() => {
		const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (prefersReducedMotion) {
			cascade = true;
			return;
		}

		const timer = window.setTimeout(() => {
			cascade = true;
		}, 1800);

		return () => window.clearTimeout(timer);
	});
</script>

<section id="stack" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-5" style="--child-i: 0">stack</p>

		<div class="flex flex-col gap-6">
			{#each stackCategories as category, catIndex}
				<div class="reveal-child" style="--child-i: {catIndex + 1}">
					<p class="mb-2.5 text-[10px] tracking-[0.1em] text-ink-faint uppercase">
						{category.label}
					</p>
					<ul class="flex flex-wrap gap-2" class:stack-cascade={cascade}>
						{#each category.skills as skill, skillIndex}
							{@const globalIndex =
								stackCategories
									.slice(0, catIndex)
									.reduce((acc, c) => acc + c.skills.length, 0) + skillIndex}
							<li>
								<span class="stack-pill" style="--pill-i: {globalIndex}">{skill}</span>
							</li>
						{/each}
					</ul>
				</div>
			{/each}
		</div>
	</div>
</section>
