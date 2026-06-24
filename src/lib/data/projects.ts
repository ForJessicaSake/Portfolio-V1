import {
	ASOWO_LINK,
	KONTRAK_LINK,
	SHOPCO_LINK,
	CLOTHING_STORE_LINK,
	INVENTORY_ADMIN_LINK,
	GOAL_TRACKER_LINK,
	GROCERY_STORE_LINK,
	STICKY_NOTES_LINK,
	SUNNY_SIDE_LINK
} from '$lib/constants/links';

export type ProjectBadge =  'case study' | 'finance' | 'ecommerce' | 'productivity' | 	null;

export interface Project {
	title: string;
	description: string;
	stack: string[];
	link: string;
	badge: ProjectBadge;
	featured?: boolean;
	muted?: boolean;
}

export const projects: Project[] = [
	{
		title: 'Àṣọwó — Personal Lending Tracker',
		description:
			'Track money lent between friends and family. Handles asymmetric trust-based lending — log amounts, set reminder schedules, see your full exposure per person. Built for how money actually moves in Nigeria.',
		stack: ['Svelte', 'Firebase', 'TypeScript'],
		link: ASOWO_LINK,
		badge: 'case study',
		featured: true
	},
	{
		title: 'Shop.co — E-commerce Storefront',
		description:
			'Full-stack ecommerce with client storefront and admin dashboard — product catalog, cart, Paystack checkout, inventory management, and JWT-secured REST APIs. Monorepo on GitHub.',
		stack: ['React', 'TypeScript', 'Node.js', 'Express', 'MongoDB', 'Paystack'],
		link: SHOPCO_LINK,
		badge: 'ecommerce'
	},
	{
		title: 'Inventory Admin — Merchant Dashboard',
		description:
			'Admin companion to Shop.co — product inventory, purchase orders, transaction management, and user administration. Same repo, separate deployable app.',
		stack: ['React', 'Node.js', 'Express', 'MongoDB', 'React Query', 'Zustand'],
		link: INVENTORY_ADMIN_LINK,
		badge: 'ecommerce',
		muted: true
	},
	{
		title: 'Goal Tracker',
		description:
			'A client application for tracking personal goal progress over time — focused on clean UX and reliable Firebase-backed persistence.',
		stack: ['Next.js', 'TypeScript', 'Firebase', 'Tailwind CSS'],
		link: GOAL_TRACKER_LINK,
		badge: "case study",
		muted: true
	},
];
