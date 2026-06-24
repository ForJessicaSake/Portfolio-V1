<script lang="ts">
	import { themeState, toggleTheme } from '$lib/stores/theme.svelte';

	const isDark = $derived(themeState.current === 'dark');
</script>

<button
	type="button"
	class="theme-toggle flex items-center gap-1.5 rounded-[3px] border border-rule px-2 py-1 text-ink-mid transition-colors duration-200 hover:border-accent hover:text-accent"
	aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
	title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
	onclick={toggleTheme}
>
	{#if isDark}
		<!-- Sun: visible action = go light -->
		<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
			<circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.75" />
			<path
				stroke="currentColor"
				stroke-width="1.75"
				stroke-linecap="round"
				d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"
			/>
		</svg>
		<span class="hidden text-[10px] tracking-wide uppercase sm:inline">Light</span>
	{:else}
		<!-- Moon crescent: visible action = go dark -->
		<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
			<path
				d="M21 14.5A8.5 8.5 0 1112.5 3a6.5 6.5 0 109.5 11.5z"
				opacity="0.95"
			/>
		</svg>
		<span class="hidden text-[10px] tracking-wide uppercase sm:inline">Dark</span>
	{/if}
</button>
