<script lang="ts">
	import { onMount } from 'svelte';
	import ThemeToggle from '$lib/components/ThemeToggle.svelte';

	const navLinks = [
		{ label: 'works', href: '#work' },
		{ label: 'projects', href: '#projects' },
		{ label: 'writing', href: '#writing' },
		{ label: 'about', href: '#about' }
	];

	let scrolled = $state(false);
	let drawerOpen = $state(false);

	onMount(() => {
		const onScroll = () => {
			scrolled = window.scrollY > 80;
		};

		window.addEventListener('scroll', onScroll, { passive: true });
		onScroll();

		return () => window.removeEventListener('scroll', onScroll);
	});

	function closeDrawer() {
		drawerOpen = false;
	}

	function toggleDrawer() {
		drawerOpen = !drawerOpen;
	}
</script>

<header
	class="nav-header fixed top-0 right-0 left-0 z-50 border-b border-transparent transition-all duration-300 ease-out"
	class:nav-scrolled={scrolled}
>
	<nav class="mx-auto flex max-w-[720px] items-center justify-between px-5 py-4 sm:px-6">
		<a href="/" class="nav-brand text-[13px] font-medium text-ink">Jessica</a>

		<div class="hidden items-center gap-5 sm:flex">
			<ul class="flex items-center gap-6">
				{#each navLinks as link}
					<li>
						<a
							href={link.href}
							class="nav-link text-[12px] text-ink-mid transition-colors duration-300 hover:text-ink"
						>
							{link.label}
						</a>
					</li>
				{/each}
				<li class="flex items-center" aria-label="Open to work">
					<span class="pulse-dot block h-[7px] w-[7px] rounded-full bg-green"></span>
				</li>
			</ul>
			<ThemeToggle />
		</div>

		<div class="flex items-center gap-3 sm:hidden">
			<ThemeToggle />
			<button
				type="button"
				class="flex h-8 w-8 flex-col items-end justify-center gap-[5px]"
				aria-label={drawerOpen ? 'Close menu' : 'Open menu'}
				aria-expanded={drawerOpen}
				onclick={toggleDrawer}
			>
				<span
					class="block h-px w-5 bg-ink transition-transform duration-200"
					class:rotate-45={drawerOpen}
					class:translate-y-[6px]={drawerOpen}
				></span>
				<span class="block h-px w-5 bg-ink transition-opacity duration-200" class:opacity-0={drawerOpen}></span>
				<span
					class="block h-px w-5 bg-ink transition-transform duration-200"
					class:-rotate-45={drawerOpen}
					class:-translate-y-[6px]={drawerOpen}
				></span>
			</button>
		</div>
	</nav>

	<aside
		class="fixed top-[57px] right-0 z-50 w-[200px] border border-rule bg-surface transition-transform duration-300 sm:hidden"
		class:translate-x-0={drawerOpen}
		class:translate-x-full={!drawerOpen}
		aria-hidden={!drawerOpen}
	>
		<ul class="flex flex-col py-2">
			{#each navLinks as link}
				<li>
					<a
						href={link.href}
						class="block px-5 py-3 text-[12px] text-ink-mid transition-colors duration-150 hover:bg-card hover:text-ink"
						onclick={closeDrawer}
					>
						{link.label}
					</a>
				</li>
			{/each}
			<li class="flex items-center gap-2 px-5 py-3">
				<span class="pulse-dot block h-[7px] w-[7px] rounded-full bg-green"></span>
				<span class="text-[11px] text-ink-faint">Open to work</span>
			</li>
		</ul>
	</aside>
</header>

<style>
	.nav-header {
		background-color: transparent;
	}

	.nav-scrolled {
		background-color: var(--nav-scrolled-bg);
		border-color: var(--theme-rule);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
	}

	.nav-scrolled .nav-brand {
		font-weight: 600;
		color: var(--theme-ink);
	}

	.nav-scrolled .nav-link {
		color: var(--theme-ink-mid);
	}
</style>
