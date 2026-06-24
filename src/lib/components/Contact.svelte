<script lang="ts">
	import { scrollReveal } from '$lib/actions/scrollReveal';
	import { CV_LINK, GITHUB_LINK, LINKEDIN_LINK, isLinkReady } from '$lib/constants/links';

	type ContactIcon = 'email' | 'github' | 'linkedin' | 'resume';

	const contacts: {
		label: string;
		display: string;
		href: string;
		icon: ContactIcon;
		ready: boolean;
	}[] = [
		{
			label: 'Email',
			display: '',
			href: 'mailto:jessicajoseph1807@gmail.com',
			icon: 'email',
			ready: true
		},
		{
			label: 'GitHub',
			display: '',
			href: GITHUB_LINK,
			icon: 'github',
			ready: isLinkReady(GITHUB_LINK)
		},
		{
			label: 'LinkedIn',
			display: '',
			href: LINKEDIN_LINK,
			icon: 'linkedin',
			ready: isLinkReady(LINKEDIN_LINK)
		},
		{
			label: 'Resume',
			display: '',
			href: CV_LINK,
			icon: 'resume',
			ready: isLinkReady(CV_LINK)
		}
	];
</script>

{#snippet contactIcon(icon: ContactIcon)}
	<span
		class="contact-icon flex h-8 w-8 shrink-0 items-center justify-center text-ink-mid transition-colors duration-180"
		aria-hidden="true"
	>
		{#if icon === 'email'}
			<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.2">
				<rect x="1.5" y="3.5" width="13" height="9" rx="1" />
				<path d="M1.5 4.5L8 9.5L14.5 4.5" />
			</svg>
		{:else if icon === 'github'}
			<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
				<path
					d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"
				/>
			</svg>
		{:else if icon === 'linkedin'}
			<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
				<path
					d="M3.5 2C2.67 2 2 2.67 2 3.5v9c0 .83.67 1.5 1.5 1.5h9c.83 0 1.5-.67 1.5-1.5v-9c0-.83-.67-1.5-1.5-1.5h-9zM5.5 12H4V7h1.5v5zM4.75 6.25c-.5 0-.9-.4-.9-.9s.4-.9.9-.9.9.4.9.9-.4.9-.9.9zM13 12h-1.5V9.25c0-.83-.02-1.9-1.16-1.9-1.16 0-1.34.9-1.34 1.84V12H7.5V7H9v.75h.03c.28-.52.96-1.07 1.98-1.07 2.12 0 2.51 1.4 2.51 3.21V12z"
				/>
			</svg>
		{:else}
			<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.2">
				<path d="M9 1.5H4.5a1 1 0 00-1 1V13.5a1 1 0 001 1h7a1 1 0 001-1V5.5L9 1.5z" />
				<path d="M9 1.5V5.5H13" />
				<path d="M5.5 8.5h5M5.5 10.5h5M5.5 12.5h3" />
			</svg>
		{/if}
	</span>
{/snippet}

{#snippet contactContent(contact: (typeof contacts)[number])}
	{@render contactIcon(contact.icon)}
	<div>
		<p class="text-[11px] text-ink-faint">{contact.label}</p>
		<p class="text-[13px] text-ink">{contact.display}</p>
	</div>
{/snippet}

<section id="contact" class="mx-auto max-w-[720px] px-5 py-12 sm:px-6 sm:py-16">
	<div class="scroll-reveal" use:scrollReveal>
		<p class="section-eyebrow reveal-child mb-5" style="--child-i: 0">get in touch</p>
		<ul class="grid grid-cols-1 gap-3 sm:grid-cols-2">
			{#each contacts as contact, i}
				<li class="reveal-child" style="--child-i: {i + 1}">
					{#if contact.ready}
						<a
							href={contact.href}
							class="contact-item"
							target={contact.icon !== 'email' ? '_blank' : undefined}
							rel={contact.icon !== 'email' ? 'noopener noreferrer' : undefined}
						>
							{@render contactContent(contact)}
						</a>
					{:else}
						<div class="contact-item opacity-50" aria-disabled="true">
							{@render contactContent(contact)}
						</div>
					{/if}
				</li>
			{/each}
		</ul>
	</div>
</section>
