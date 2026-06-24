export interface Article {
	title: string;
	publication: string;
	description: string;
	url: string;
	date: string;
}

export const articles: Article[] = [
	{
		title: 'The Safest Way To Hide Your API Keys When Using React',
		publication: 'Smashing Magazine',
		description:
			'Environment variables, backend proxy servers, and key management — a practical guide to keeping API keys out of your client bundle.',
		url: 'https://www.smashingmagazine.com/2023/05/safest-way-hide-api-keys-react/',
		date: 'May 2023'
	},
	// {
	// 	title: 'Managing complex forms in React using Formik and Yup',
	// 	publication: 'Frontend Mentor',
	// 	description:
	// 		'Schema-based validation, conditional fields, and form state management — walking through a real sign-up form challenge.',
	// 	url: 'https://www.frontendmentor.io/articles/managing-complex-forms-in-react-using-formik-and-yup-C2DlPAsgp6',
	// 	date: 'Feb 2024'
	// },
	// {
	// 	title: 'Static Site Generation Vs Server Side Rendering',
	// 	publication: 'OpenReplay',
	// 	description:
	// 		'When to pre-render at build time vs generate on each request — performance trade-offs for Next.js and modern web apps.',
	// 	url: 'https://blog.openreplay.com/static-side-generation-vs-server-side-rendering/',
	// 	date: '2023'
	// },
	{
		title: "You Don't Need A State Management Library — Use UseState Plus Context",
		publication: 'OpenReplay',
		description:
			'Why React Context + useState is enough for most apps, and when reaching for Zustand or Redux actually makes sense.',
		url: 'https://blog.openreplay.com/you-dont-need-a-state-management-library--use-ustate-plus-context/',
		date: '2023'
	},
	// {
	// 	title: 'How to Create a Slider in JavaScript',
	// 	publication: 'Turing',
	// 	description:
	// 		'Building image sliders from scratch — autoplay, navigation controls, and DOM manipulation without libraries.',
	// 	url: 'https://www.turing.com/kb/how-to-create-slider-in-js',
	// 	date: '2023'
	// },
	// {
	// 	title: 'How to Check Type of Objects & Variables in TypeScript',
	// 	publication: 'Turing',
	// 	description:
	// 		'typeof, instanceof, and the in operator — narrowing union types and checking object shapes safely in TypeScript.',
	// 	url: 'https://www.turing.com/kb/check-type-of-objects-variables-in-typescript',
	// 	date: '2023'
	// }
];
