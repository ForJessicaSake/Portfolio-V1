export type Theme = 'dark' | 'light';

export const themeState = $state<{ current: Theme }>({ current: 'dark' });

export function setTheme(next: Theme) {
	themeState.current = next;
	if (typeof document !== 'undefined') {
		document.documentElement.setAttribute('data-theme', next);
		localStorage.setItem('theme', next);
	}
}

export function toggleTheme() {
	setTheme(themeState.current === 'dark' ? 'light' : 'dark');
}

export function initTheme() {
	if (typeof window === 'undefined') return;

	const stored = localStorage.getItem('theme');
	if (stored === 'light' || stored === 'dark') {
		themeState.current = stored;
	} else {
		themeState.current = window.matchMedia('(prefers-color-scheme: light)').matches
			? 'light'
			: 'dark';
	}

	document.documentElement.setAttribute('data-theme', themeState.current);
}
