<script lang="ts">
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { experience } from '$lib/data/experience';
</script>

<section id="work" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-5" style="--child-i: 0">experience</p>
		<ul class="divide-y divide-rule">
			{#each experience as job, i}
				<li class="work-row reveal-child py-4" style="--child-i: {i + 1}">
					<div class="mb-2 flex items-baseline justify-between gap-6">
						<div class="min-w-0">
							<p class="text-[13px] leading-snug">
								<span class="font-medium text-ink">{job.company}</span>
								<span class="text-ink-faint"> · </span>
								<span class="text-ink-mid">{job.role}</span>
							</p>
						</div>
						<p class="shrink-0 text-[11px] tracking-wide text-ink-faint uppercase">{job.date}</p>
					</div>
					<p class="max-w-[580px] text-[12px] leading-[1.7] text-ink-mid">{job.description}</p>
				</li>
			{/each}
		</ul>
	</div>
</section>
