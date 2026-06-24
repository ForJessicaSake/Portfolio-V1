export const stackCategories = [
	{
		label: 'Frontend',
		skills: [
			'JavaScript (ES6+)',
			'TypeScript',
			'React.js',
			'Next.js',
			'Svelte',
			'HTML5',
			'CSS3',
			'Tailwind CSS'
		]
	},
	{
		label: 'State Management',
		skills: ['Context API', 'Zustand', 'Jotai', 'React Query']
	},
	{
		label: 'Backend & Services',
		skills: [
			'Node.js',
			'NestJS',
			'Fastify',
			'Express.js',
			'Python',
			'RESTful APIs',
			'MongoDB',
			'Mongoose',
			'PostgreSQL',
			'Redis',
			'RabbitMQ',
			'Firebase',
			'Supabase',
			'Sanity CMS'
		]
	},
	{
		label: 'Testing & CI/CD',
		skills: ['Playwright', 'Jest', 'E2E Testing', 'Integration Testing', 'GitHub Actions']
	},
	{
		label: 'Forms & Validation',
		skills: ['React Hook Form', 'Formik', 'Yup', 'Zod']
	},
	{
		label: 'Payments',
		skills: ['Stripe', 'Paystack', 'Fincra', 'Escrow Systems']
	},
	{
		label: 'Messaging & Notifications',
		skills: ['Twilio', 'WhatsApp API', 'Email Templates', 'OTP Auth']
	},
	{
		label: 'Tools & Workflow',
		skills: ['Git', 'GitHub', 'GitLab', 'Bitbucket', 'Figma', 'Jira', 'Notion', 'Trello', 'GoHighLevel']
	},
	{
		label: 'AI-Assisted Development',
		skills: ['Cursor', 'GitHub Copilot', 'Claude']
	}
] as const;

/** Flat list for cascade animation index */
export const allStackSkills = stackCategories.flatMap((c) => c.skills);
