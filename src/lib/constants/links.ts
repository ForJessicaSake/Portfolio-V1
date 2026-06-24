/** Live URLs — search for PLACEHOLDER strings when adding new links. */
export const CV_LINK =
	'https://docs.google.com/document/d/1jq3GaEUt7BW1rr0THMsSVst2qijhFLw98pjOKQ3BTDE/view';
export const GITHUB_LINK = 'https://github.com/ForJessicaSake';
export const LINKEDIN_LINK = 'https://www.linkedin.com/in/jessica-ekpo/';
export const ASOWO_LINK = '[ASOWO_LINK_PLACEHOLDER]';
export const KONTRAK_LINK = '[KONTRAK_LINK_PLACEHOLDER]';
export const SHOPCO_LINK = 'https://github.com/ForJessicaSake/Shop.co-ecommerce-store';
export const CLOTHING_STORE_LINK = 'https://github.com/ForJessicaSake/Shop.co-ecommerce-store';
export const INVENTORY_ADMIN_LINK = 'https://github.com/ForJessicaSake/Shop.co-ecommerce-store';
export const GOAL_TRACKER_LINK = 'https://github.com/ForJessicaSake/GoalTracker';
export const GROCERY_STORE_LINK = '[GROCERY_STORE_LINK_PLACEHOLDER]';
export const STICKY_NOTES_LINK = '[STICKY_NOTES_LINK_PLACEHOLDER]';
export const SUNNY_SIDE_LINK = '[SUNNY_SIDE_LINK_PLACEHOLDER]';
export const SITE_URL = 'https://jessicas-portfolio.vercel.app';
export const OG_IMAGE = `${SITE_URL}/og.png`;

export function isLinkReady(url: string): boolean {
	return !url.startsWith('[');
}
