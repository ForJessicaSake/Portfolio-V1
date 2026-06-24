export interface ExperienceEntry {
	company: string;
	role: string;
	description: string;
}

export const experience: ExperienceEntry[] = [
	{
		company: 'Peerless',
		role: 'Frontend Engineer',
		description:
			'Enterprise technology for banks and financial institutions — building the digital infrastructure behind modern Islamic and conventional finance products.'
	},
	{
		company: 'EventFlutter',
		role: 'Backend Engineer',
		description:
			'Event management platform connecting creators, vendors, venue owners, and attendees — from discovery to ticketing to day-of coordination.'
	},
	{
		company: 'Daply',
		role: 'Fullstack Engineer',
		description:
			'SaaS platform for team workflows, bug tracking, and sales automation — helping teams replace scattered tools with one structured system.'
	},
	{
		company: 'KiaKia Finance',
		role: 'Frontend Engineer',
		description:
			'Fintech platform providing payment infrastructure, virtual accounts, and merchant finance tools for businesses across Nigeria.'
	},
	{
		company: 'Brimble',
		role: 'Frontend Engineer',
		description:
			'Developer tooling platform for deploying and hosting web applications — making it simple for teams to ship and scale on the web.'
	}
];
