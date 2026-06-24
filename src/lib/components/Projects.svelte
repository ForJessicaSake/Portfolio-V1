<script lang="ts">
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { projects } from '$lib/data/projects';
	import { isLinkReady } from '$lib/constants/links';

	function handleCardClick(link: string, ready: boolean) {
		if (ready) {
			window.open(link, '_blank', 'noopener,noreferrer');
		}
	}

	function handleKeydown(e: KeyboardEvent, link: string, ready: boolean) {
		if ((e.key === 'Enter' || e.key === ' ') && ready) {
			e.preventDefault();
			window.open(link, '_blank', 'noopener,noreferrer');
		}
	}
</script>

<section id="projects" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-5" style="--child-i: 0">projects</p>
		<ul class="flex flex-col gap-4">
			{#each projects as project, i}
				{@const ready = isLinkReady(project.link)}
				<li class="reveal-child" style="--child-i: {i + 1}">
					<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
					<div
						role={ready ? 'link' : 'article'}
						tabindex={ready ? 0 : undefined}
						class="proj-card rounded-[6px] p-5"
						class:featured={project.featured}
						class:cursor-pointer={ready}
						class:opacity-80={project.muted}
						onclick={() => handleCardClick(project.link, ready)}
						onkeydown={(e) => handleKeydown(e, project.link, ready)}
					>
						<span
							class="absolute top-5 right-5 text-[14px] transition-colors duration-150"
							class:text-ink-faint={!ready}
							class:text-ink-mid={ready}
							aria-hidden="true"
						>
							↗
						</span>

						<div class="relative mb-2 flex items-center gap-2 pr-6">
							<h3 class="text-[15px] font-medium text-ink">{project.title}</h3>
							{#if project.badge === 'finance'}
								<span
									class="rounded-[3px] bg-green-tint px-1.5 py-0.5 text-[10px] tracking-wide text-green uppercase"
								>
									finance
								</span>
							{:else if project.badge === 'ecommerce'}
								<span
									class="rounded-[3px] bg-amber-tint px-1.5 py-0.5 text-[10px] tracking-wide text-accent uppercase"
								>
									ecommerce
								</span>
							{:else if project.badge === 'case study'}
								<span
									class="rounded-[3px] border border-rule px-1.5 py-0.5 text-[10px] tracking-wide text-ink-faint uppercase"
								>
									case study
								</span>
							{/if}
						</div>

						<p class="relative mb-4 text-[13px] leading-[1.65] text-ink-mid">{project.description}</p>

						<ul class="relative flex flex-wrap gap-2">
							{#each project.stack as tag}
								<li>
									<span class="text-[11px] text-ink-faint">{tag}</span>
								</li>
							{/each}
						</ul>
					</div>
				</li>
			{/each}
		</ul>
	</div>
</section>
