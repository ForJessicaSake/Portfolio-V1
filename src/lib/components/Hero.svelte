<script lang="ts">
	import { CV_LINK } from '$lib/constants/links';

	const line1 = ['Building', 'real', 'products'];
	const line2 = ['people', 'actually', 'use.'];
	const wordCount = line1.length + line2.length;
</script>

<section
	id="hero"
	class="mx-auto max-w-[720px] bg-bg px-5 pt-28 pb-16 sm:px-6 sm:pt-32 sm:pb-20"
	style="--word-count: {wordCount}"
>
	<p class="hero-eyebrow section-eyebrow mb-5">Software Engineer · Lagos, Nigeria</p>

	<h1 class="mb-6 font-serif text-[28px] leading-[1.15] text-ink sm:text-[34px] lg:text-[42px]">
		<span class="block">
			{#each line1 as word, i}
				<span class="hero-word-wrap">
					<span class="hero-word-inner" style="--word-i: {i}">{word}</span>
				</span>
				{#if i < line1.length - 1}{' '}{/if}
			{/each}
		</span>
		<span class="mt-1 block pl-6 italic text-accent-warm sm:pl-8 lg:pl-[52px]">
			{#each line2 as word, j}
				<span class="hero-word-wrap">
					<span class="hero-word-inner" style="--word-i: {line1.length + j}">{word}</span>
				</span>
				{#if j < line2.length - 1}{' '}{/if}
			{/each}
		</span>
	</h1>

	<p class="hero-body mb-8 max-w-[420px] text-[14px] leading-[1.75] text-ink-mid">
		3+ years shipping production software across fintech, SaaS, and developer tooling. I specialise in
	   complex step flows, real-time systems, reconciliation dashboards, where the
		engineering has to disappear and only the experience remains.
	</p>

	<div class="flex flex-col gap-3 sm:flex-row sm:gap-4">
		<a href="#work" class="hero-btn btn-fill w-full sm:w-auto">view work</a>
		<a
			href={CV_LINK}
			class="hero-btn btn-ghost w-full sm:w-auto"
			target="_blank"
			rel="noopener noreferrer"
		>
			view CV
		</a>
	</div>
</section>
