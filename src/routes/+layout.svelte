<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { onMount } from 'svelte';
	import { initTheme } from '$lib/stores/theme.svelte';
	import {
		GITHUB_LINK,
		LINKEDIN_LINK,
		SITE_URL,
		OG_IMAGE,
		isLinkReady
	} from '$lib/constants/links';

	let { children } = $props();

	onMount(() => {
		initTheme();
	});

	const siteReady = isLinkReady(SITE_URL);
	const githubReady = isLinkReady(GITHUB_LINK);
	const linkedinReady = isLinkReady(LINKEDIN_LINK);

	const sameAs = [githubReady ? GITHUB_LINK : null, linkedinReady ? LINKEDIN_LINK : null].filter(
		(link): link is string => link !== null
	);

	const jsonLd = {
		'@context': 'https://schema.org',
		'@type': 'Person',
		name: 'Jessica',
		jobTitle: 'Software Engineer',
		...(siteReady ? { url: SITE_URL } : {}),
		email: 'jessicajoseph1807@gmail.com',
		address: {
			'@type': 'PostalAddress',
			addressLocality: 'Lagos',
			addressCountry: 'Nigeria'
		},
		...(sameAs.length > 0 ? { sameAs } : {})
	};
</script>

<svelte:head>
	<title>Jessica — Software Engineer</title>
	<link rel="icon" href={favicon} />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600&display=swap"
		rel="stylesheet"
	/>
	<meta
		name="description"
		content="Jessica Ekpo is a Software Engineer with 3+ years building production fintech, SaaS, and developer tooling products. Based in Lagos, Nigeria."
	/>
	<meta
		name="keywords"
		content="Jessica Ekpo, Software Engineer, Frontend Engineer, Fullstack Engineer, React, Next.js, Svelte, TypeScript, Fintech, Lagos, Nigeria"
	/>
	<meta property="og:title" content="Jessica Ekpo — Software Engineer" />
	<meta
		property="og:description"
		content="3+ years shipping production software across fintech, SaaS, and developer tooling. Based in Lagos, Nigeria."
	/>
	<meta property="og:type" content="website" />
	<meta property="og:url" content={SITE_URL} />
	<meta property="og:image" content={OG_IMAGE} />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="@forJessica_sake" />
	<meta name="twitter:title" content="Jessica Ekpo — Software Engineer" />
	<meta
		name="twitter:description"
		content="3+ years shipping production software across fintech, SaaS, and developer tooling."
	/>
	<meta name="twitter:image" content={OG_IMAGE} />
	{#if siteReady}
		<link rel="canonical" href={SITE_URL} />
	{/if}
	{@html `<script type="application/ld+json">${JSON.stringify(jsonLd)}<\/script>`}
</svelte:head>

{@render children()}
