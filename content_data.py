
# Content Data for Auratekk Website
# Structured dictionary containing content for all 31 subpages.

content_data = {
    # --- Top Level Pages ---
    'technologies.html': {
        'hero_image': 'hero_emerging_tech_ai_1770688470055.png',
        'title': 'Our Technologies',
        'intro': "At Aura Tech, we don't just follow trends; we leverage the most powerful, scalable, and secure technologies to build digital solutions that last. Our stack is chosen for performance, reliability, and future-readiness.",
        'services': [
            {
                'title': 'Frontend Excellence', 
                'desc': 'React.js, Vue.js, Angular, and Next.js for blazing-fast, interactive user interfaces.',
                'details': {
                    'long_desc': "We craft pixel-perfect, responsive, and accessible user interfaces using the latest modern frameworks. Our focus is on component reusability, state management efficiency, and minimizing load times to ensure your users have a seamless experience across all devices.",
                    'quote': "The interface is the product.",
                    'bullet_title': 'Key Capabilities',
                    'bullets': ['Single Page Applications (SPA)', 'Server-Side Rendering (SSR)', 'Progressive Web Apps (PWA)', 'Micro-frontend Architecture'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Backend Powerhouses', 
                'desc': 'Node.js, Python (Django/Flask), and Go for robust, scalable server-side logic.',
                'details': {
                    'long_desc': "Behind every great app is a powerful backend. We architect scalable, secure, and high-performance server-side systems. Whether it's a microservices architecture or a robust monolith, we choose the right tool for the job to ensure your business logic runs smoothly.",
                    'quote': "Logic that scales with your ambition.",
                    'bullet_title': 'Core Technologies',
                    'bullets': ['RESTful & GraphQL APIs', 'Microservices & Docker', 'Real-time WebSockets', 'Authentication (OAuth/JWT)'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Mobile Native & Cross-Platform', 
                'desc': 'Swift (iOS), Kotlin (Android), React Native, and Flutter for seamless mobile experiences.',
                'details': {
                    'long_desc': "Reach your users wherever they are. We build native apps for peak performance and cross-platform solutions for speed-to-market. Our mobile development process prioritizes touch-responsive UI, offline capabilities, and battery efficiency.",
                    'quote': "Your business in their pocket.",
                    'bullet_title': 'Mobile Strengths',
                    'bullets': ['Native iOS & Android', 'React Native / Flutter', 'App Store Optimization', 'IoT Integration'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Cloud & DevOps', 
                'desc': 'AWS, Azure, Google Cloud, Docker, and Kubernetes for resilient infrastructure.',
                'details': {
                    'long_desc': "Infrastructure that heals itself. We implement CI/CD pipelines, infrastructure-as-code, and auto-scaling cloud architectures. This ensures your application can handle traffic spikes without downtime and updates are deployed rapidly and safely.",
                    'quote': "Deploy faster, sleep better.",
                    'bullet_title': 'Cloud Features',
                    'bullets': ['AWS / Azure / GCP', 'Kubernetes Orchestration', 'CI/CD Pipelines', 'Serverless Functions'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Database Technologies', 
                'desc': 'PostgreSQL, MongoDB, Redis, and Supabase for secure and efficient data management.',
                'details': {
                    'long_desc': "Data is your most valuable asset. We design schemas that are normalized, indexed, and optimized for your specific query patterns. from relational reliability to NoSQL flexibility, we ensure data integrity and speed.",
                    'quote': "Information architecture done right.",
                    'bullet_title': 'Data Solutions',
                    'bullets': ['Relational (SQL) Design', 'NoSQL Document Stores', 'In-Memory Caching', 'Data Warehousing'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Emerging Tech', 
                'desc': 'TensorFlow, PyTorch (AI/ML), Solidity (Blockchain), and Unity (AR/VR).',
                'details': {
                    'long_desc': "Future-proof your business with cutting-edge tech. We experiment and implement AI models, blockchain smart contracts, and immersive AR/VR experiences that give you a competitive edge in a rapidly evolving digital landscape.",
                    'quote': "Innovation is not optional.",
                    'bullet_title': 'Future Tech',
                    'bullets': ['Generative AI Models', 'Smart Contracts', 'Immersive AR/VR', 'Predictive Analytics'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }
        ],
        'benefits': {
            'title': 'Why Our Tech Stack Matters',
            'items': [
                'Scalability to grow with your business.',
                'Security by design, not as an afterthought.',
                'Performance optimization for superior user experience.',
                'Maintainability to reduce long-term costs.'
            ]
        }
    },
    'industries.html': {
        'hero_image': 'hero_future_city_general_1770688485783.png',
        'title': 'Industries We Serve',
        'intro': "Digital transformation looks different for every sector. We bring specialized knowledge and tailored solutions to distinct industries, understanding their unique challenges and regulatory landscapes.",
        'services': [
            {
                'title': 'FinTech & Banking', 
                'desc': 'Secure transaction systems, neobanking apps, and fraud detection algorithms.',
                'details': {
                    'long_desc': "We engineer banking solutions that prioritize security without compromising user experience. From KYC onboarding flows to high-frequency trading platforms, our systems are compliant, fast, and bulletproof against threats.",
                    'quote': "Secure finance for a digital world.",
                    'bullet_title': 'FinTech Solutions',
                    'bullets': ['Digital Wallets', 'Payment Gateways', 'Fraud Detection AI', 'Regulatory Compliance'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            },
            {
                'title': 'Healthcare & MedTech', 
                'desc': 'HIPAA-compliant telemedicine platforms, EMR integration, and AI diagnostics.',
                'details': {
                    'long_desc': "Improving patient outcomes through technology. We build telemedicine apps, patient portals, and interoperable systems that securely share health data between providers, labs, and patients.",
                    'quote': "Care connected.",
                    'bullet_title': 'HealthTech',
                    'bullets': ['Telemedicine Apps', 'EMR/EHR Integration', 'IoT Health Monitoring', 'Data Privacy (HIPAA)'],
                    'image': 'service_startup_1770395129627.png'
                }
            },
            {
                'title': 'Real Estate', 
                'desc': 'Virtual tour platforms, property management systems, and smart contract integration.',
                'details': {
                    'long_desc': "Transforming how properties are bought, sold, and managed. We build platforms featuring 3D virtual tours, automated lease management, and blockchain-based property records for transparency.",
                    'quote': "Property meets technology.",
                    'bullet_title': 'PropTech',
                    'bullets': ['Virtual Tours (VR)', 'Property Mgmt Systems', 'Smart Contracts', 'Listing Portals'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            },
            {
                'title': 'E-Commerce & Retail', 
                'desc': 'High-conversion online stores, inventory management, and omnichannel experiences.',
                'details': {
                    'long_desc': "Retail is no longer just physical. We create unified commerce experiences that track customers across channels, manage inventory in real-time, and personalize recommendations to boost basket size.",
                    'quote': "Commerce without boundaries.",
                    'bullet_title': 'Retail Tech',
                    'bullets': ['Omnichannel Platforms', 'Inventory Sync', 'Personalization Engines', 'Loyalty Programs'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Logistics & Supply Chain', 
                'desc': 'Real-time tracking, route optimization, and fleet management solutions.',
                'details': {
                    'long_desc': "Efficiency in motion. Our logistics solutions use GPS, IoT, and AI to optimize routes, track shipments in real-time, and predict maintenance needs for fleets, saving time and fuel.",
                    'quote': "Optimization in motion.",
                    'bullet_title': 'Logistics Tech',
                    'bullets': ['Fleet Management', 'Route Optimization', 'Last-Mile Delivery', 'IoT Tracking'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Education (EdTech)', 
                'desc': 'Interactive learning management systems (LMS) and virtual classrooms.',
                'details': {
                    'long_desc': "Learning beyond the classroom. We build engaging LMS platforms, gamified learning apps, and virtual classrooms that make education accessible and interactive for students of all ages.",
                    'quote': "Knowledge availability.",
                    'bullet_title': 'EdTech Features',
                    'bullets': ['LMS Platforms', 'Gamification', 'Virtual Classrooms', 'Progress Tracking'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
            'title': 'Industry-Specific Expertise',
            'items': [
                'Compliance with industry regulations (GDPR, HIPAA, etc.).',
                'User experiences tailored to specific customer behaviors.',
                'Integration with legacy industry systems.',
                'Data-driven insights relevant to your market.'
            ]
        }
    },
    'about-us.html': {
        'hero_image': 'hero_future_city_general_1770688485783.png',
        'title': 'About Aura Tech',
        'intro': "Aura Tech is a premier digital transformation agency based in Dubai, UAE. We bridge the gap between visionary ideas and technical reality. We are a team of engineers, designers, and strategists committed to engineering digital excellence.",
        'services': [
             {
                 'title': 'Our Mission', 
                 'desc': 'To empower businesses with innovative technology that drives tangible growth and efficiency.',
                 'details': {
                     'long_desc': "Our mission is simple yet ambitious: to be the catalyst for your digital evolution. We don't just build software; we build solutions that solve real-world problems and open up new opportunities for revenue and growth.",
                     'quote': "Empowering growth.",
                     'bullet_title': 'Mission Pillars',
                     'bullets': ['Innovation', 'Integrity', 'Impact', 'Excellence'],
                     'image': 'hero_future_city_general_1770688485783.png'
                 }
             },
             {
                 'title': 'Our Vision', 
                 'desc': 'To be the leading architect of the digital future in the MENA region and beyond.',
                 'details': {
                     'long_desc': "We envision a future where technology is seamless, invisible, and empowering. As we grow, we aim to set the standard for digital engineering in the Middle East, fostering a hub of innovation and talent in Dubai.",
                     'quote': "Architecting the future.",
                     'bullet_title': 'Future Goals',
                     'bullets': ['Regional Leadership', 'Global Standards', 'Talent Incubation', 'Sustainable Tech'],
                     'image': 'hero_future_city_general_1770688485783.png'
                 }
             },
             {
                 'title': 'Our Approach', 
                 'desc': 'Agile, transparent, and collaborative. We view ourselves as your long-term technology partner.',
                 'details': {
                    'long_desc': "We believe in co-creation. Our agile methodology ensures you are involved at every step, from initial discovery to final deployment. We maintain open lines of communication and transparent reporting.",
                    'quote': "Partnership, not just a vendor.",
                    'bullet_title': 'How We Work',
                    'bullets': ['Agile Methodology', 'Weekly Sprints', 'Transparent Comms', 'Long-term Support'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
             }
        ],
        'benefits': {
            'title': 'The Aura Tech Difference',
            'items': [
                'Deep regional market understanding combined with global standards.',
                'Full-cycle development from concept to support.',
                'A culture of continuous innovation and learning.',
                'Client-centric delivery focused on ROI.'
            ]
        }
    },
    'careers.html': {
        'hero_image': 'hero_software_dev_matrix_1770688395055.png',
        'title': 'Join the Future',
        'intro': "We are always looking for passionate problem-solvers, creative thinkers, and tech enthusiasts. If you want to work on challenging projects that shape the digital landscape, Aura Tech is the place for you.",
        'services': [
             {
                 'title': 'Culture of Innovation', 
                 'desc': 'Experiment with new technologies and push boundaries.',
                 'details': {
                     'long_desc': "We encourage experimentation. Whether it's trying out a new JS framework, diving into AI, or optimizing a database query, we support learning. Fail fast, learn faster, and build better.",
                     'quote': "Fail fast, learn faster.",
                     'bullet_title': 'Culture Check',
                     'bullets': ['Hackathons', 'R&D Time', 'Open Source', 'Knowledge Sharing'],
                     'image': 'hero_web_dev_futuristic_1770688377502.png'
                 }
             },
             {
                 'title': 'Growth & Learning', 
                 'desc': 'Continuous mentorship, workshops, and access to learning resources.',
                 'details': {
                     'long_desc': "Your growth is our growth. We provide budgets for courses, conferences, and certifications. Senior engineers mentor juniors, and we hold regular internal tech talks to share knowledge.",
                     'quote': "Always be learning.",
                     'bullet_title': 'Perks',
                     'bullets': ['Learning Budget', 'Certifications', 'Mentorship', 'Tech Talks'],
                     'image': 'hero_marketing_creative_1770688454386.png'
                 }
             },
             {
                 'title': 'Work-Life Balance', 
                 'desc': 'Flexible working, remote options, and a supportive team environment.',
                 'details': {
                     'long_desc': "Burnout helps no one. We believe in flexible hours and output over hours at the desk. We respect your time off and ensure you have the recharge time needed to do your best work.",
                     'quote': "Work smart, live well.",
                     'bullet_title': 'Balance',
                     'bullets': ['Remote Options', 'Flexible Hours', 'Paid Time Off', 'Team Retreats'],
                     'image': 'hero_future_city_general_1770688485783.png'
                 }
             }
        ],
        'benefits': {
             'title': 'Current Openings',
             'items': [
                 'Senior Full Stack Developer (React/Node)',
                 'UI/UX Designer',
                 'DevOps Engineer',
                 'Project Manager'
             ]
        }
    },

    # --- Web Development ---
    'services/web-development.html': {
        'hero_image': 'hero_web_dev_futuristic_1770688377502.png',
        'title': 'Custom Web Development',
        'intro': "Your website is your digital headquarters. We build high-performance, responsive, and secure web applications tailored to your specific business needs. From complex enterprise portals to dynamic single-page applications (SPAs).",
        'services': [
            {
                'title': 'Single Page Applications (SPA)', 
                'desc': 'Fast, fluid user experiences using React, Vue, or Angular.',
                'details': {
                    'long_desc': "We build SPAs that load once and perform like native apps. By dynamically rewriting the current page rather than loading entire new pages from a server, we ensure a silky-smooth user experience that keeps engagement high.",
                    'quote': "No more page reloads.",
                    'bullet_title': 'SPA Benefits',
                    'bullets': ['Instant Interactions', 'Reduced Bandwidth', 'Rich User Experience', 'Easy Scale-up'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Progressive Web Apps (PWA)', 
                'desc': 'Websites that offer app-like experiences, offline capabilities, and installability.',
                'details': {
                    'long_desc': "Bridge the gap between web and mobile. Our PWAs are installable on home screens, work offline, and send push notifications, giving you the reach of the web with the engagement of a native app.",
                    'quote': "The best of both worlds.",
                    'bullet_title': 'PWA Features',
                    'bullets': ['Offline Mode', 'Push Notifications', 'Home Screen Install', 'App-like Performance'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Enterprise Web Portals', 
                'desc': 'Scalable, secure internal tools and customer-facing portals.',
                'details': {
                    'long_desc': "Empower your organization with custom portals. Whether it's a customer self-service dashboard, an employee intranet, or a supply chain management tool, we build secure, role-based systems that streamline operations.",
                    'quote': "Centralize your operations.",
                    'bullet_title': 'Portal Capabilities',
                    'bullets': ['Role-Based Access', 'Data Visualization', 'Workflow Automation', 'Secure Document Mgmt'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'API Development & Integration', 
                'desc': 'Robust RESTful and GraphQL APIs to connect your systems.',
                'details': {
                    'long_desc': "Connectivity is key. We design and document API strategies that allow your disparate systems to talk to each other. From payment gateways to CRM integrations, we ensure data flows securely and efficiently.",
                    'quote': "The glue of the internet.",
                    'bullet_title': 'Integration Types',
                    'bullets': ['REST & GraphQL', 'Third-party Webhooks', 'Legacy System Wrapping', 'Public API Design'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }
        ],
        'benefits': {
            'title': 'Why Choose Custom Development?',
            'items': [
                'Complete control over features and functionality.',
                'Optimized performance for better SEO and user retention.',
                'Scalability to handle growing traffic and data.',
                'Enhanced security tailored to your specific risks.'
            ]
        }
    },
    'services/wordpress-development.html': {
        'hero_image': 'hero_web_dev_futuristic_1770688377502.png',
        'title': 'WordPress Development',
        'intro': "Powering over 40% of the web, WordPress is a versatile content management system. We go beyond themes, creating custom, high-speed, and secure WordPress solutions that give you control over your content without compromising on performance.",
        'services': [
            {
                'title': 'Custom Theme Development', 
                'desc': 'Pixel-perfect themes built from scratch to match your brand identity.',
                'details': {
                    'long_desc': "Don't settle for templates. We design and code bespoke WordPress themes that are lightweight, SEO-friendly, and perfectly aligned with your brand guidelines. No bloat, just performance.",
                    'quote': "Unique as your brand.",
                    'bullet_title': 'Theme Features',
                    'bullets': ['Gutenberg Compatibility', 'ACF Pro Integration', 'Schema Markup', 'Accessibility Ready'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Plugin Development', 
                'desc': 'Custom functionality extensions tailored to your unique requirements.',
                'details': {
                    'long_desc': "Need functionality that doesn't exist? We write custom plugins to extend WordPress capabilities. From complex calculators to integration with proprietary external APIs, we build it to standard.",
                    'quote': "Extend your reach.",
                    'bullet_title': 'Plugin Types',
                    'bullets': ['API Integrations', 'Custom Post Types', 'User Portals', 'Data Migration Tools'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'WooCommerce Solutions', 
                'desc': 'Scalable e-commerce stores built on the robust WooCommerce platform.',
                'details': {
                    'long_desc': "Sell anything, anywhere. We build high-converting WooCommerce stores with custom checkouts, subscription models, and complex shipping logic, ensuring a seamless buying experience.",
                    'quote': "Sell smarter.",
                    'bullet_title': 'WooCommerce Features',
                    'bullets': ['Custom Checkout', 'Subscription Logic', 'Payment Gateway Setup', 'Inventory Sync'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'WordPress Security & Optimization', 
                'desc': 'Hardening security, optimizing database queries, and reducing load times.',
                'details': {
                    'long_desc': "A slow or hacked site costs money. We perform deep optimization and security hardening, including database cleaning, image compression, and firewall setup to keep your WP site blazing fast and safe.",
                    'quote': "Fast and fortress-like.",
                    'bullet_title': 'Optimization Tasks',
                    'bullets': ['Core Web Vitals', 'Malware Removal', 'Caching Setup', 'Database Tuning'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }
        ],
        'benefits': {
            'title': 'WordPress Done Right',
            'items': [
                'Easy content management for non-technical teams.',
                'SEO-friendly structure out of the box.',
                'Huge ecosystem of integrations.',
                'Cost-effective rapid deployment.'
            ]
        }
    },
    'services/ecommerce-development.html': {
        'hero_image': 'hero_web_dev_futuristic_1770688377502.png',
        'title': 'E-Commerce Development',
        'intro': "We build digital storefronts that convert. Whether you need a custom headless solution or a robust platform-based store, we create seamless shopping experiences that drive sales and retain customers.",
        'services': [
            {
                'title': 'Custom E-Commerce Platforms', 
                'desc': 'Tailored solutions for unique business models using MERN or Python stacks.',
                'details': {
                    'long_desc': "When off-the-shelf isn't enough. We build fully custom e-commerce platforms that handle unique product configurations, complex B2B logic, or multivendor marketplaces.",
                    'quote': "Commerce without limits.",
                    'bullet_title': 'Custom Features',
                    'bullets': ['B2B Portals', 'Multivendor Marketplaces', 'Subscription Engines', 'Auction Systems'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Headless Commerce', 
                'desc': 'Decoupling frontend and backend for ultimate flexibility and speed (Shopify Plus, BigCommerce).',
                'details': {
                    'long_desc': "Speed meets flexibility. By separating the frontend from the backend, we can deliver ultra-fast shopping experiences (PWA) while using robust engines like Shopify Plus or BigCommerce for backend management.",
                    'quote': "Unmatched speed.",
                    'bullet_title': 'Headless Stacks',
                    'bullets': ['Shopify Hydrogen', 'Next.js Commerce', 'Swell / Medusa', 'Contentful Integration'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Payment Gateway Integration', 
                'desc': 'Secure integration with Stripe, PayPal, Tap, PayTabs, and regional gateways.',
                'details': {
                    'long_desc': "Secure the transaction. We assist in selecting and integrating the right payment gateways for your region and business model, ensuring compliance (PCI-DSS) and smooth checkout flows.",
                    'quote': "Get paid, securely.",
                    'bullet_title': 'Gateways',
                    'bullets': ['Stripe / PayPal', 'Regional (Tap, PayTabs)', 'Crypto Payments', 'Buy Now Pay Later'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Recommendation Engines', 
                'desc': 'AI-driven product suggestions to increase average order value.',
                'details': {
                    'long_desc': "Know what they want before they do. We implement AI algorithms that analyze user behavior to suggest relevant products, increasing cross-sells and upsells automatically.",
                    'quote': "Personalized shopping.",
                    'bullet_title': 'AI Features',
                    'bullets': ['Personalized Feeds', 'Similar Products', 'Dynamic Pricing', 'Cart Recovery'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }
        ],
        'benefits': {
            'title': 'Drive Revenue Growth',
            'items': [
                'Optimized checkout flows to reduce cart abandonment.',
                'Mobile-first design for the modern shopper.',
                'Automated inventory and order management.',
                'Advanced analytics to track performance.'
            ]
        }
    },
    'services/custom-cms-development.html': {
        'hero_image': 'hero_web_dev_futuristic_1770688377502.png',
        'title': 'Custom CMS Development',
        'intro': "Off-the-shelf CMS solutions simpler don't fit every business. We architect custom Content Management Systems that align perfectly with your internal workflows, data structures, and publishing needs.",
        'services': [
            {
                'title': 'Headless CMS', 
                'desc': 'Implementation of Strapi, Sanity, or Contentful for omnichannel content delivery.',
                'details': {
                    'long_desc': "Content for every screen. A headless CMS allows you to manage content in one place and deploy it to websites, mobile apps, smartwatches, and kiosks simultaneously via API.",
                    'quote': "Create once, publish everywhere.",
                    'bullet_title': 'Platforms',
                    'bullets': ['Strapi', 'Sanity.io', 'Contentful', 'Directus'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Enterprise Content Management', 
                'desc': 'Systems for managing large volumes of documents and media securely.',
                'details': {
                    'long_desc': "Organize the chaos. We build ECM systems that handle millions of documents with advanced search, versioning, and access controls, suitable for legal, healthcare, and corporate environments.",
                    'quote': "Total information control.",
                    'bullet_title': 'ECM Features',
                    'bullets': ['OCR & Indexing', 'Version Control', 'Audit Trails', 'Granular Permissions'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Workflow Automation', 
                'desc': 'Custom approval chains, scheduling, and publishing workflows.',
                'details': {
                    'long_desc': " streamline your editorial process. We define and implement custom workflows that ensure content is reviewed, approved, and scheduled by the right people at the right time.",
                    'quote': "Efficiency built-in.",
                    'bullet_title': 'Workflow Tools',
                    'bullets': ['Visual Drag-and-Drop', 'Email Notifications', 'Role-Based Dashboards', 'Scheduling Calendar'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Migration Services', 
                'desc': 'Seamlessly moving your data from legacy systems to modern architectures.',
                'details': {
                    'long_desc': "Upgrade without data loss. We map, transform, and migrate your content from legacy proprietary systems to modern, open standards, ensuring SEO rankings and data integrity are preserved.",
                    'quote': "Move forward safely.",
                    'bullet_title': 'Migration Steps',
                    'bullets': ['Data Mapping', 'Automated Scripts', 'Validation Testing', 'SEO 301 Redirects'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            }
        ],
        'benefits': {
            'title': 'Control Your Narrative',
            'items': [
                'Streamlined workflows that save your team time.',
                'Scalable architecture for growing content libraries.',
                'Decoupled frontend for design freedom.',
                'Enhanced security with granular role-based access.'
            ]
        }
    },

    # --- Software Development ---
    'services/custom-software-development.html': {
        'hero_image': 'hero_software_dev_matrix_1770688395055.png',
        'title': 'Custom Software Development',
        'intro': "We engineer bespoke software solutions that solve complex business problems. From automation tools to data processing engines, we build software that becomes a competitive advantage.",
        'services': [
            {
                'title': 'SaaS Product Development', 
                'desc': 'End-to-end development of scalable Software-as-a-Service products.',
                'details': {
                    'long_desc': "Turn your idea into a subscription revenue machine. We handle the entire SaaS lifecycle, from multi-tenant architecture and billing integration to user onboarding and admin dashboards.",
                    'quote': "Scale your revenue.",
                    'bullet_title': 'SaaS Components',
                    'bullets': ['Multi-tenancy', 'Subscription Billing', 'User Management', 'Admin Dashboards'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Internal Business Tools', 
                'desc': 'Dashboards, CRMs, and ERPS tailored to your operational needs.',
                'details': {
                    'long_desc': "Spreadsheets only go so far. We build custom internal tools that perfectly match your workflows, automating data entry, generating reports, and providing real-time visibility into your KPIs.",
                    'quote': "Operations, streamlined.",
                    'bullet_title': 'Toof Features',
                    'bullets': ['Custom CRM/ERP', 'Inventory Mgmt', 'HR Portals', 'Data Dashboards'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Legacy Modernization', 
                'desc': 'Refactoring and re-platforming outdated software to modern tech stacks.',
                'details': {
                    'long_desc': "Don't let tech debt hold you back. We analyze your legacy codebase and incrementally refactor or rewrite it using modern, maintainable technologies, improving performance and security without breaking business continuity.",
                    'quote': "Modernize, don't just maintain.",
                    'bullet_title': 'Modernization',
                    'bullets': ['Code Refactoring', 'Cloud Migration', 'UI/UX Refresh', 'Database Migration'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Desktop Application Development', 
                'desc': 'Cross-platform desktop apps using Electron or native frameworks.',
                'details': {
                    'long_desc': "Power on the desktop. We build cross-platform desktop applications using Electron or .NET MAUI that offer deep system integration, offline capabilities, and high performance for heavy-duty tasks.",
                    'quote': "Native power.",
                    'bullet_title': 'Desktop Tech',
                    'bullets': ['Electron/Tauri', '.NET MAUI', 'Offline Support', 'Hardware Access'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }
        ],
        'benefits': {
            'title': 'Software That Fits',
            'items': [
                'Eliminate manual processes and reduce errors.',
                'Data integration across disparate systems.',
                'Ownership of intellectual property.',
                'Built to scale with your organization.'
            ]
        }
    },
    'services/mvp-development.html': {
        'hero_image': 'hero_software_dev_matrix_1770688395055.png',
        'title': 'MVP Development',
        'intro': "Got a startup idea? We help you validate it fast. Our MVP (Minimum Viable Product) development service focuses on building the core features needed to launch, test, and iterate quickly.",
        'services': [
            {
                'title': 'Product Discovery & Strategy', 
                'desc': 'Defining the core value proposition and feature set.',
                'details': {
                    'long_desc': "Start on the right foot. We work with you to distill your vision into a concrete product roadmap, identifying the 'must-have' features that deliver immediate value to your early adopters.",
                    'quote': "Validate before you build.",
                    'bullet_title': 'Discovery Phase',
                    'bullets': ['User Personas', 'Feature Mapping', 'Competitor Analysis', 'Tech Stack Selection'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Rapid Prototyping', 
                'desc': 'Clickable UI/UX prototypes to test flows before coding.',
                'details': {
                    'long_desc': "See it to believe it. We create high-fidelity interactive prototypes that simulate the final product, allowing you to pitch to investors and get user feedback without writing a single line of code.",
                    'quote': "Visualize the vision.",
                    'bullet_title': 'Prototype Tools',
                    'bullets': ['Figma/Adobe XD', 'Interactive Flows', 'User Testing', 'Investor Decks'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Agile Development', 
                'desc': 'Fast sprints to get a functional product to market in weeks, not months.',
                'details': {
                    'long_desc': "Speed is a feature. Our agile teams work in short sprints to deliver shippable code every week, ensuring total transparency and allowing you to pivot quickly based on market feedback.",
                    'quote': "Launch fast.",
                    'bullet_title': 'Agile Process',
                    'bullets': ['Weekly Sprints', 'CI/CD Pipelines', 'TDD (Test Driven)', 'Regular Demos'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            },
            {
                'title': 'Launch Support', 
                'desc': 'Technical support during your go-live and initial user onboarding.',
                'details': {
                    'long_desc': "We don't just ship and leave. We monitor your launch, handle immediate bug fixes, and scale infrastructure as your user base grows, ensuring your first impression is a great one.",
                    'quote': "Smooth liftoff.",
                    'bullet_title': 'Launch Ops',
                    'bullets': ['Server Monitoring', 'Bug Triage', 'Performance Tuning', 'Analytics Setup'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }
        ],
        'benefits': {
            'title': 'Start Smart',
            'items': [
                'Minimize initial investment and risk.',
                'Faster time-to-market.',
                'Gather real user feedback early.',
                'Solid foundation for future scalability.'
            ]
        }
    },
    'services/devops-services.html': {
        'hero_image': 'hero_software_dev_matrix_1770688395055.png',
        'title': 'DevOps Services',
        'intro': "Bridge the gap between development and operations. We implement CI/CD pipelines, automated testing, and infrastructure-as-code to speed up release cycles and improve software reliability.",
        'services': [
            {
                'title': 'CI/CD Pipeline Setup', 
                'desc': 'Automated build, test, and deployment workflows (Jenkins, GitHub Actions, GitLab CI).',
                'details': {
                    'long_desc': "Automate everything. We set up robust pipelines that automatically build, test, and deploy your code every time you commit, reducing manual errors and freeing up developers to write code.",
                    'quote': "Push to deploy.",
                    'bullet_title': 'Pipeline Tools',
                    'bullets': ['GitHub Actions', 'GitLab CI', 'Jenkins', 'CircleCI'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Infrastructure as Code (IaC)', 
                'desc': 'Managing infrastructure using Terraform or CloudFormation.',
                'details': {
                    'long_desc': "Treat servers like software. We define your entire infrastructure in code, allowing you to provision, modify, and destroy environments reliably and repeatably in minutes.",
                    'quote': "Reproducible infra.",
                    'bullet_title': 'IaC Tech',
                    'bullets': ['Terraform', 'AWS CloudFormation', 'Ansible', 'Pulumi'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Containerization', 
                'desc': 'Dockerizing applications and orchestrating with Kubernetes.',
                'details': {
                    'long_desc': "Ship anywhere. We package your applications into lightweight containers that run consistently across development, testing, and production environments, eliminating 'it works on my machine' issues.",
                    'quote': "Consistency everywhere.",
                    'bullet_title': 'Container Tech',
                    'bullets': ['Docker', 'Kubernetes (K8s)', 'Helm Charts', 'Container Registries'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Monitoring & Logging', 
                'desc': 'Setting up Prometheus, Grafana, and ELK stack for real-time insights.',
                'details': {
                    'long_desc': "Visibility is power. We implement comprehensive monitoring stacks that give you real-time dashboards of your system health, application performance, and error logs.",
                    'quote': "Know your system.",
                    'bullet_title': 'Observability',
                    'bullets': ['Prometheus/Grafana', 'ELK Stack', 'New Relic', 'Sentry'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }
        ],
        'benefits': {
            'title': 'Accelerate Delivery',
            'items': [
                'Faster deployment frequency.',
                'Lower failure rate of new releases.',
                'Faster mean time to recovery (MTTR).',
                'Improved collaboration between teams.'
            ]
        }
    },

    # --- Mobile App ---
    'services/ios-app-development.html': {
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png',
        'title': 'iOS App Development',
        'intro': "Tap into the premium Apple user base with high-quality native iOS applications. We adhere to Apple's Human Interface Guidelines to create apps that feel right at home on iPhone and iPad.",
        'services': [
            {
                'title': 'Native Swift Development', 
                'desc': 'Using the latest Swift features for performance and safety.',
                'details': {
                    'long_desc': "We build 100% native iOS apps using Swift and SwiftUI. This ensures maximum performance, access to the latest APIs (like ARKit, CoreML), and a user experience that feels perfectly at home on any iPhone or iPad.",
                    'quote': "Built for Apple silicon.",
                    'bullet_title': 'iOS Tech',
                    'bullets': ['Swift & SwiftUI', 'CoreData / Realm', 'XCTest / UI Testing', 'Combine / RxSwift'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'iPadOS & watchOS Apps', 
                'desc': 'Extending your reach to the wider Apple ecosystem.',
                'details': {
                    'long_desc': "Don't stop at the phone. We design and build apps specifically optimized for the large canvas of the iPad and the quick-glance utility of the Apple Watch, providing a holistic ecosystem experience.",
                    'quote': "Ecosystem completeness.",
                    'bullet_title': 'Platforms',
                    'bullets': ['iPadOS Multitasking', 'Apple Watch Complications', 'tvOS Apps', 'WidgetKit'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'App Store Optimization (ASO)', 
                'desc': 'Helping your app get discovered.',
                'details': {
                    'long_desc': "A great app needs to be found. We optimize your App Store listing with the right keywords, compelling screenshots, and preview videos to improve search visibility and conversion rates.",
                    'quote': "Get found first.",
                    'bullet_title': 'ASO Steps',
                    'bullets': ['Keyword Research', 'Visual Optimization', 'A/B Testing Listings', 'Review Management'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Maintenance & Updates', 
                'desc': 'Keeping your app compatible with the latest iOS versions.',
                'details': {
                    'long_desc': "iOS changes every year. We provide ongoing maintenance to ensure your app remains compatible with new iOS updates, screen sizes, and privacy requirements, preventing crashes and bad reviews.",
                    'quote': "Always up to date.",
                    'bullet_title': 'Maintenance',
                    'bullets': ['iOS Version updates', 'Bug Fixes', 'Performance Monitoring', 'Library Updates'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            }
        ],
        'benefits': {
             'title': 'Premium Experience',
             'items': [
                 'Best-in-class performance and animation.',
                 'Access to latest device hardware features.',
                 'High security and data privacy.',
                 'Seamless integration with Apple services.'
             ]
        }
    },
    'services/android-app-development.html': {
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png',
        'title': 'Android App Development',
        'intro': "Reach the global majority with robust native Android apps. We build apps that run smoothly across the fragmented landscape of devices, screen sizes, and OS versions.",
        'services': [
            {
                'title': 'Native Kotlin Development', 
                'desc': 'Modern, concise, and safe code for Android apps.',
                'details': {
                    'long_desc': "Kotlin is the future of Android. We write clean, concise, and safe Kotlin code to build apps that are stable, easy to maintain, and leverage the full power of the Android SDK.",
                    'quote': "Modern Android dev.",
                    'bullet_title': 'Android Tech',
                    'bullets': ['Kotlin Coroutines', 'Jetpack Compose', 'Room Database', 'Dagger/Hilt'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Material Design Implementation', 
                'desc': 'Creating intuitive UIs that follow Google design standards.',
                'details': {
                    'long_desc': "We utilize Google's Material Design 3 guidelines to create interfaces that are intuitive, accessible, and beautiful. Dynamic colors, adaptive layouts, and meaningful motion come standard.",
                    'quote': "Design that adapts.",
                    'bullet_title': 'Design features',
                    'bullets': ['Material You', 'Dark Theme Support', 'Adaptive Layouts', 'Motion Layout'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Google Play Publishing', 
                'desc': 'Navigating the submission and review process.',
                'details': {
                    'long_desc': "We handle the complexities of the Google Play Console. From setting up store listings and content ratings to managing rollouts and analyzing crash reports, we ensure a smooth release.",
                    'quote': "Release with confidence.",
                    'bullet_title': 'Play Store',
                    'bullets': ['Release Management', 'Crashlytics', 'User Feedback', 'Policy Compliance'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'IoT & Wearable Integration', 
                'desc': 'Connecting with smart devices and wearables.',
                'details': {
                    'long_desc': "Extend your app to the physical world. We build apps that communicate with Wear OS watches, IoT smart home devices, and Bluetooth peripherals for connected experiences.",
                    'quote': "Connected ecosystem.",
                    'bullet_title': 'Integrations',
                    'bullets': ['Wear OS', 'Bluetooth LE', 'Smart Home APIs', 'NFC Features'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            }
        ],
        'benefits': {
             'title': 'Global Reach',
             'items': [
                 'Target the largest mobile OS market share.',
                 'Flexible customization options.',
                 'Easy integration with Google ecosystem.',
                 'Wide device compatibility.'
             ]
        }
    },
    'services/react-native-development.html': {
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png',
        'title': 'React Native Development',
        'intro': "Build once, run everywhere. React Native allows us to create native-feeling apps for both iOS and Android using a single codebase, significantly reducing development time and cost.",
        'services': [
            {
                'title': 'Cross-Platform Apps', 
                'desc': 'Unified codebase for iOS and Android.',
                'details': {
                    'long_desc': "One  codebase, two platforms. We use React Native to build apps that share up to 90% of their code between iOS and Android, drastically reducing specific development time and maintenance costs.",
                    'quote': "Code once, ship twice.",
                    'bullet_title': 'RN Benefits',
                    'bullets': ['Shared Codebase', 'Faster Time-to-Market', 'Simplified Maintenance', 'Web React Consistency'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Component-Based UI', 
                'desc': 'Reusable UI components for consistent design.',
                'details': {
                    'long_desc': "We build modular UI libraries. By creating reusable components, we ensure design consistency across your app and make future updates and feature additions incredibly fast.",
                    'quote': "Modular design.",
                    'bullet_title': 'Component Tech',
                    'bullets': ['Styled Components', 'Storybook', 'Atomic Design', 'Theme Management'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Native Module Integration', 
                'desc': 'Bridging native code when specific performance is needed.',
                'details': {
                    'long_desc': "No limits. When React Native's standard APIs aren't enough, we write custom native bridges in Swift or Kotlin to access low-level device features or optimize heavy calculations.",
                    'quote': "Power without compromise.",
                    'bullet_title': 'Native Bridge',
                    'bullets': ['Swift/Kotlin Modules', 'Camera/GPS Access', 'Background Tasks', 'Native SDKs'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Migration to React Native', 
                'desc': 'Porting existing native apps to React Native.',
                'details': {
                    'long_desc': "Unified legacy apps. We can migrate your separate iOS and Android apps to a single React Native codebase, simplifying your engineering operations and unifying your feature roadmap.",
                    'quote': "Unify your stack.",
                    'bullet_title': 'Migration',
                    'bullets': ['Code Analysis', 'Feature Parity', 'Data Migration', 'Team Training'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }
        ],
        'benefits': {
             'title': 'Efficiency & Speed',
             'items': [
                 'Faster development cycle.',
                 'Cost-effective (shared codebase).',
                 'Live reloading for rapid iteration.',
                 'Large community and ecosystem support.'
             ]
        }
    },
    'services/flutter-app-development.html': {
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png',
        'title': 'Flutter App Development',
        'intro': "Create beautiful, natively compiled applications from a single codebase using Google's Flutter UI toolkit. Flutter is known for its expressive UI and near-native performance.",
        'services': [
            {
                'title': 'Custom Widget Creation', 
                'desc': 'Building unique, brand-specific UI elements.',
                'details': {
                    'long_desc': "In Flutter, everything is a widget. We build custom, pixel-perfect widgets that perfectly match your brand's design system, regardless of the underlying platform's native controls.",
                    'quote': "Pixel perfect everywhere.",
                    'bullet_title': 'Widget Magic',
                    'bullets': ['Custom Animations', 'Material/Cupertino', 'Brand Consistent', 'High Performance'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Cross-Platform Development', 
                'desc': 'Deploy to iOS, Android, Web, and Desktop.',
                'details': {
                    'long_desc': "Truly universal. With Flutter 3, we can target iOS, Android, Web, Windows, macOS, and Linux from a single project, giving you the widest possible reach with one engineering team.",
                    'quote': "Run everywhere.",
                    'bullet_title': 'Targets',
                    'bullets': ['Mobile (iOS/Android)', 'Web Apps', 'Desktop (Win/Mac/Lin)', 'Embedded Systems'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Legacy App Modernization', 
                'desc': 'Revamping old apps with Flutter\'s modern UI capabilities.',
                'details': {
                    'long_desc': "Give old apps new life. We can incrementally add Flutter screens to your existing native apps to modernize the UI/UX without a complete rewrite, or rewrite completely for a fresh start.",
                    'quote': "Modernize incrementally.",
                    'bullet_title': 'Integration',
                    'bullets': ['Add-to-App', 'UI Overhaul', 'Performance Boost', 'Unified Logic'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            },
            {
                'title': 'Desktop & Web Support', 
                'desc': 'Extending mobile apps to larger screens.',
                'details': {
                    'long_desc': "Adapt to any screen. We design responsive Flutter layouts that adapt gracefully from a watch face up to a 4K monitor, ensuring your app looks great on any device.",
                    'quote': "Adaptive design.",
                    'bullet_title': 'Responsive',
                    'bullets': ['Adaptive Layouts', 'Keyboard/Mouse Support', 'Large Screen UI', 'PWA Support'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Beautiful & Fast',
             'items': [
                 'Expressive and flexible UI.',
                 'Native performance (compiled code).',
                 'Single codebase for mobile, web, and desktop.',
                 'Hot reload for instant updates.'
             ]
        }
    },

    # --- Other Services ---
    'services/branding-design.html': {
        'hero_image': 'hero_marketing_creative_1770688454386.png',
        'title': 'Branding & Design',
        'intro': "Your brand is more than a logo; it's an experience. We craft compelling visual identities and user interfaces (UI/UX) that tell your story and resonate with your target audience.",
        'services': [
            {
                'title': 'Brand Strategy & Identity', 
                'desc': 'Logo design, color palettes, typography, and brand guidelines.',
                'details': {
                    'long_desc': "We define who you are. From mission statements to visual systems, we build brands that have a clear voice, a distinct look, and a lasting emotional connection with customers.",
                    'quote': "Define your essence.",
                    'bullet_title': 'Identity Kit',
                    'bullets': ['Logo Design', 'Visual Guidelines', 'Tone of Voice', 'Stationery Design'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'UI/UX Design', 
                'desc': 'Wireframing, prototyping, and high-fidelity interface design.',
                'details': {
                    'long_desc': "Design that works. We don't just make things look pretty; we design intuitive user flows and accessible interfaces that guide users to action and make complex tasks simple.",
                    'quote': "Form meets function.",
                    'bullet_title': 'UX Process',
                    'bullets': ['User Research', 'Wireframing', 'Interactive Prototypes', 'Usability Testing'],
                    'image': 'service_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Graphic Design', 
                'desc': 'Marketing collateral, social media assets, and illustrations.',
                'details': {
                    'long_desc': "Visuals that convert. From social media posts to pitch decks and print materials, we create high-quality assets that maintain brand consistency and grab attention.",
                    'quote': "Visual impact.",
                    'bullet_title': 'Design Assets',
                    'bullets': ['Social Media Graphics', 'Pitch Decks', 'Infographics', 'Print Marketing'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Motion Graphics', 
                'desc': 'Animated logos and UI interactions to bring designs to life.',
                'details': {
                    'long_desc': "Move your audience. We use animation to explain complex concepts, add delight to user interactions, and make your brand content shareable and engaging.",
                    'quote': "Bring it to life.",
                    'bullet_title': 'Motion Services',
                    'bullets': ['Logo Animation', 'Explainer Videos', 'Micro-interactions', 'Social Stories'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            }
        ],
        'benefits': {
             'title': 'Stand Out',
             'items': [
                 'Consistent brand presence across channels.',
                 'Intuitive user experiences that convert.',
                 'Professional aesthetic builds trust.',
                 'Memorable visual storytelling.'
             ]
        }
    },
    'services/digital-marketing.html': {
        'hero_image': 'hero_marketing_creative_1770688454386.png',
        'title': 'Digital Marketing',
        'intro': "Great tech needs to be seen. Our data-driven digital marketing strategies help you reach your audience, drive traffic, and generate qualified leads.",
        'services': [
            {
                'title': 'Search Engine Optimization (SEO)', 
                'desc': 'On-page, off-page, and technical SEO to improve organic rankings.',
                'details': {
                    'long_desc': "Be found by intent. We optimize your website's structure, content, and authority to climb the search engine rankings for keywords that matter to your business.",
                    'quote': "Rank higher.",
                    'bullet_title': 'SEO Tactics',
                    'bullets': ['Technical Audits', 'Keyword Strategy', 'Backlink Building', 'Local SEO'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Pay-Per-Click (PPC)', 
                'desc': 'Targeted Google Ads and social media advertising campaigns.',
                'details': {
                    'long_desc': "Instant traffic. We create highly targeted ad campaigns on Google, LinkedIn, and Instagram that maximize your ROAS (Return on Ad Spend) and bring in qualified leads immediately.",
                    'quote': "Targeted reach.",
                    'bullet_title': 'Ad Platforms',
                    'bullets': ['Google Search Ads', 'LinkedIn B2B', 'Meta (FB/Insta)', 'Remarketing'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Content Marketing', 
                'desc': 'Creating valuable content that attracts and engages users.',
                'details': {
                    'long_desc': "Authority through value. We create blog posts, whitepapers, and case studies that solve your customers' problems, establishing your brand as a thought leader in the industry.",
                    'quote': "Educate to sell.",
                    'bullet_title': 'Content Types',
                    'bullets': ['Blog Strategy', 'Whitepapers', 'Case Studies', 'Email Newsletters'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Social Media Management', 
                'desc': 'Building community and engagement on platforms like LinkedIn and Instagram.',
                'details': {
                    'long_desc': "Build your tribe. We manage your social media presence, creating a regular cadence of engaging posts, interacting with followers, and growing your community.",
                    'quote': "Engage your community.",
                    'bullet_title': 'Social Services',
                    'bullets': ['Content Calendar', 'Community Mgmt', 'Influencer Outreach', 'Analytics Reports'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ],
        'benefits': {
             'title': 'Grow Your Business',
             'items': [
                 'Measurable ROI on marketing spend.',
                 'Targeted reach to your ideal customer.',
                 'Increased brand awareness.',
                 'Consistent lead generation pipeline.'
             ]
        }
    },
    'services/emerging-tech.html': {
        'hero_image': 'hero_emerging_tech_ai_1770688470055.png',
        'title': 'Emerging Tech (AI/AR/VR)',
        'intro': "Stay ahead of the curve. We help you explore and implement cutting-edge technologies like Artificial Intelligence, Augmented Reality, and Virtual Reality to create futuristic experiences.",
        'services': [
            {
                'title': 'AI & Machine Learning', 
                'desc': 'Predictive analytics, chatbots, and automation solutions.',
                'details': {
                    'long_desc': "Intelligence, automated. We build custom ML models for predictive analytics, NLP chatbots for improved customer support, and automation scripts to handle repetitive tasks.",
                    'quote': "Smarter business.",
                    'bullet_title': 'AI Solutions',
                    'bullets': ['Predicitive Analytics', 'NLP / Chatbots', 'Computer Vision', 'Process Automation'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            },
            {
                'title': 'Augmented Reality (AR)', 
                'desc': 'Interactive product visualizations and marketing experiences.',
                'details': {
                    'long_desc': "Enhance reality. We build web-based (WebAR) and app-based AR experiences that let customers try products virtually, gamify marketing campaigns, and interact with your brand in 3D.",
                    'quote': "Layered reality.",
                    'bullet_title': 'AR Use Cases',
                    'bullets': ['Virtual Try-On', 'Interactive Packaging', 'Location-based AR', 'WebAR'],
                    'image': 'hero_future_city_general_1770688485783.png'
                }
            },
            {
                'title': 'Virtual Reality (VR)', 
                'desc': 'Immersive training simulations and virtual showrooms.',
                'details': {
                    'long_desc': "Full immersion. We develop VR experiences for corporate training, real estate walkthroughs, and virtual showrooms that transport users to entirely new worlds.",
                    'quote': "Immersive worlds.",
                    'bullet_title': 'VR Applications',
                    'bullets': ['Training Sims', 'Virtual Tours', 'Product Showrooms', 'Gaming Experiences'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Blockchain Integration', 
                'desc': 'Smart contracts and decentralized application (dApp) development.',
                'details': {
                    'long_desc': "Trustless systems. We help you integrate blockchain technology where it adds value, such as supply chain transparency, secure identity management, or tokenized assets.",
                    'quote': "Decentralized trust.",
                    'bullet_title': 'Web3 Tech',
                    'bullets': ['Smart Contracts', 'NFT Integration', 'DeFi Protocols', 'Private Blockchains'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }
        ],
        'benefits': {
             'title': 'Future-Proof',
             'items': [
                 'Early adopter advantage.',
                 'Innovative customer engagement.',
                 'Operational efficiency through AI.',
                 'New revenue streams.'
             ]
        }
    },
    'services/cloud-consulting.html': {
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png',
        'title': 'Cloud Consulting',
        'intro': "Navigate the cloud with confidence. We help you design, implement, and optimize cloud architectures on AWS, Azure, or Google Cloud that are secure, cost-effective, and scalable.",
        'services': [
            {
                'title': 'Cloud Strategy & Migration', 
                'desc': 'Planning and executing your move to the cloud.',
                'details': {
                    'long_desc': "Map your journey. We assess your current infrastructure and business goals to create a strategic roadmap for cloud adoption, ensuring you choose the right providers and services.",
                    'quote': "Strategic cloud adoption.",
                    'bullet_title': 'Strategy Steps',
                    'bullets': ['Readiness Assessment', 'TCO Analysis', 'Provider Selection', 'Migration Roadmap'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Cloud Architecture Design', 
                'desc': 'Building resilient, high-availability systems.',
                'details': {
                    'long_desc': "Architected for failure. We design cloud environments using best practices for high availability, fault tolerance, and security, ensuring your applications stay up no matter what.",
                    'quote': "Resilient by design.",
                    'bullet_title': 'Architecture',
                    'bullets': ['Multi-AZ Setup', 'Load Balancing', 'Auto-scaling Groups', 'Disaster Recovery'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Cost Optimization', 
                'desc': 'Analyzing and reducing cloud spend.',
                'details': {
                    'long_desc': "Stop overpaying. We audit your cloud usage and implement cost-saving measures like reserved instances, right-sizing resources, and eliminating waste.",
                    'quote': "Efficient spending.",
                    'bullet_title': 'optimization',
                    'bullets': ['Resource Right-sizing', 'Spot Instances', 'Budget Alerts', 'Waste Elimination'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Serverless Computing', 
                'desc': 'Leveraging Lambda/Functions for scalable event-driven apps.',
                'details': {
                    'long_desc': "No servers to manage. We build event-driven applications using serverless technologies, allowing you to pay only for the compute time you actually use.",
                    'quote': "Pay per execution.",
                    'bullet_title': 'Serverless',
                    'bullets': ['AWS Lambda', 'Azure Functions', 'Google Cloud Run', 'EventBridge'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }
        ],
        'benefits': {
             'title': 'Cloud Agility',
             'items': [
                 'Scalability on demand.',
                 'Reduced IT infrastructure costs.',
                 'Global reach and low latency.',
                 'Enhanced disaster recovery capabilities.'
             ]
        }
    },

    # --- Infrastructure ---
    'services/it-infrastructure-setup.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'IT Infrastructure Setup',
        'intro': "A solid foundation is key to business continuity. We design and deploy robust IT infrastructure, from structured cabling to server room setup, ensuring your physical and digital backbone is reliable.",
        'services': [
            {
                'title': 'Network Design & Cabling', 
                'desc': 'Structured cabling (Cat6/Fiber) and Wi-Fi deployment.',
                'details': {
                    'long_desc': "Connectivity starts here. We design and install high-performance copper and fiber optic cabling systems, along with enterprise-grade Wi-Fi networks, ensuring dead-zone-free connectivity throughout your facility.",
                    'quote': "Solid connections.",
                    'bullet_title': 'Cabling Services',
                    'bullets': ['Structured Cabling', 'Fiber Optics', 'Wi-Fi Heatmapping', 'Switching & Routing'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Server Room Setup', 
                'desc': 'Racks, cooling, and power management solutions.',
                'details': {
                    'long_desc': "The heart of your IT. We professionally outfit server rooms with organized racking, precision cooling, and uninterruptible power supplies (UPS) to keep your critical hardware running optimally.",
                    'quote': "Cool and powered.",
                    'bullet_title': 'Server Room',
                    'bullets': ['Rack Installation', 'Cable Management', 'Precision Cooling', 'UPS & Power Gen'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Hardware Procurement', 
                'desc': 'Sourcing and installing servers, workstations, and networking gear.',
                'details': {
                    'long_desc': "The right tools for the job. We have partnerships with major hardware vendors (Dell, HP, Cisco) to source, configure, and install the best servers, workstations, and networking equipment for your needs.",
                    'quote': "Enterprise hardware.",
                    'bullet_title': 'Procurement',
                    'bullets': ['Servers & Storage', 'Workstations/Laptops', 'Networking Gear', 'Peripherals'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Virtualization', 
                'desc': 'VMware or Hyper-V setup to maximize hardware utilization.',
                'details': {
                    'long_desc': "Do more with less. We implement server virtualization using VMware or Hyper-V, allowing you to run multiple virtual servers on a single physical machine, reducing hardware costs and energy consumption.",
                    'quote': "Hardware efficiency.",
                    'bullet_title': 'Virtual Tech',
                    'bullets': ['VMware vSphere', 'Microsoft Hyper-V', 'Virtual Desktop (VDI)', 'Failover Clustering'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ],
        'benefits': {
             'title': 'Reliable Backbone',
             'items': [
                 'High network availability and speed.',
                 'Organized and scalable physical setup.',
                 'Reduced hardware footprint via virtualization.',
                 'Future-ready infrastructure.'
             ]
        }
    },
    'services/on-prem-cloud-setup.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'On-Prem & Cloud Setup',
        'intro': "Choosing between on-premise and cloud isn't always binary. We specialize in Hybrid IT environments, seamlessly integrating your on-premise legacy systems with modern cloud capabilities.",
        'services': [
            {
                'title': 'Hybrid Cloud Architecture', 
                'desc': 'Connecting local data centers with public cloud resources.',
                'details': {
                    'long_desc': "Bridge the gap. We connect your on-premise servers with public cloud providers like AWS or Azure, allowing you to burst workloads to the cloud or use cloud storage for backups while keeping sensitive data local.",
                    'quote': "Seamless hybrid.",
                    'bullet_title': 'Hybrid Tech',
                    'bullets': ['Direct Connect', 'Azure ExpressRoute', 'Hybrid Identity', 'Workload Mobility'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Private Cloud Setup', 
                'desc': 'Building internal clouds for maximum control and security.',
                'details': {
                    'long_desc': "Cloud benefits, local control. We build private cloud infrastructures using technologies like OpenStack or Azure Stack, giving you the self-service and agility of the cloud within your own secure data center.",
                    'quote': "Your own cloud.",
                    'bullet_title': 'Private Stack',
                    'bullets': ['OpenStack', 'Azure Stack HCI', 'Software Defined Network', 'Self-service Portal'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Data Synchronization', 
                'desc': 'Ensuring consistent data across on-prem and cloud environments.',
                'details': {
                    'long_desc': "Truth everywhere. We implement real-time or scheduled data synchronization solutions to ensure your users and applications always have access to the latest data, regardless of where it lives.",
                    'quote': "Data consistency.",
                    'bullet_title': 'Sync Tools',
                    'bullets': ['Database Replication', 'File Sync', 'API Gateways', 'Conflict Resolution'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'VPN & secure connectivity', 
                'desc': 'Secure tunnels between your offices and cloud resources.',
                'details': {
                    'long_desc': "Secure highways. We configure site-to-site VPNs and SD-WAN solutions to create encrypted tunnels between your branch offices, data centers, and cloud VPCs, ensuring traffic remains private.",
                    'quote': "Encrypted tunnels.",
                    'bullet_title': 'Connectivity',
                    'bullets': ['Site-to-Site VPN', 'Client VPN', 'SD-WAN', 'MPLS Integration'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }
        ],
        'benefits': {
             'title': 'Best of Both Worlds',
             'items': [
                 'Regulatory compliance (data residency).',
                 'Low latency for local applications.',
                 'Scalability of the public cloud.',
                 'Flexibility to move workloads as needed.'
             ]
        }
    },
    'services/server-network-mgmt.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'Server & Network Mgmt',
        'intro': "Keep your systems running at peak performance. Our managed server and network services ensure your critical infrastructure is updated, secure, and optimized 24/7.",
        'services': [
            {
                'title': 'Server Administration', 
                'desc': 'OS patching, user management, and performance tuning (Windows/Linux).',
                'details': {
                    'long_desc': "Expert oversight. Our admins handle the day-to-day management of your Windows and Linux servers, performing critical updates, managing user permissions, and tuning performance for optimal speed.",
                    'quote': "Running smoothly.",
                    'bullet_title': 'Admin Tasks',
                    'bullets': ['User Management', 'Patch Deployment', 'Performance Tuning', 'Log Analysis'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Network Monitoring', 
                'desc': 'Real-time tracking of bandwidth, latency, and device health.',
                'details': {
                    'long_desc': "Eyes on the network. We monitor your switches, routers, and firewalls 24/7, identifying bottlenecks or failures before they impact your business operations.",
                    'quote': "24/7 Eyes.",
                    'bullet_title': 'Monitoring',
                    'bullets': ['Bandwidth Usage', 'Device Up/Down', 'Latency Checks', 'Alerting System'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Active Directory Management', 
                'desc': 'Managing user identities and access policies.',
                'details': {
                    'long_desc': "Identity control. We manage your Active Directory or LDAP environment, ensuring user accounts are created, modified, and disabled securely, and that Group Policies are applied correctly.",
                    'quote': "Secure identities.",
                    'bullet_title': 'AD Services',
                    'bullets': ['User Provisioning', 'Group Policy (GPO)', 'SSO Configuration', 'Audit Trails'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Switch & Router Configuration', 
                'desc': 'VLAN setup, routing protocols, and firewall rules.',
                'details': {
                    'long_desc': "Traffic control. We configure your core networking equipment to segment traffic for security (VLANs), optimize routing paths, and block unauthorized access via ACLs.",
                    'quote': "Optimized traffic.",
                    'bullet_title': 'Net Config',
                    'bullets': ['VLAN Segmentation', 'QoS Policies', 'Routing Protocols', 'Firewall Rules'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ],
        'benefits': {
             'title': 'Maximum Uptime',
             'items': [
                 'Proactive issue resolution.',
                 'Optimal network performance.',
                 'Secure user access control.',
                 'Reduced downtime risk.'
             ]
        }
    },
    'services/hosting-management.html': {
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png',
        'title': 'Hosting Management',
        'intro': "Stop worrying about server uptime. We provide fully managed hosting solutions for your websites and applications, ensuring speed, security, and automated backups.",
        'services': [
            {
                'title': 'Managed Web Hosting', 
                'desc': 'Optimized environments for WordPress, Magento, and custom apps.',
                'details': {
                    'long_desc': "Fast and secure. We provide managed hosting environments tuned specifically for your application stack, whether it's WordPress, Magento, or a custom Node.js app, ensuring lightning-fast load times.",
                    'quote': "Optimized hosting.",
                    'bullet_title': 'Hosting Specs',
                    'bullets': ['SSD Storage', 'CDN Integration', 'WAF Protection', 'Daily Backups'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Dedicated Servers', 
                'desc': 'High-performance bare metal servers for resource-intensive workloads.',
                'details': {
                    'long_desc': "Raw power. For demanding applications, we provision single-tenant bare metal servers, giving you 100% of the hardware resources for maximum performance and isolation.",
                    'quote': "Bare metal power.",
                    'bullet_title': 'Dedicated',
                    'bullets': ['Full Root Access', 'Custom Hardware', 'No Noisy Neighbors', 'High Bandwidth'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'VPS Management', 
                'desc': 'Scalable virtual private servers with full root access.',
                'details': {
                    'long_desc': "Flexible scaling. Our managed VPS solutions offer a balance of cost and performance, allowing you to easily scale resources up or down as your traffic grows.",
                    'quote': "Scalable compute.",
                    'bullet_title': 'VPS Features',
                    'bullets': ['Root Access', 'Instant Scaling', 'Snapshot Backups', 'OS Choice'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Domain & DNS Management', 
                'desc': 'Secure registration and DNS configuration services.',
                'details': {
                    'long_desc': "Your address on the web. We handle domain registration, renewals, and complex DNS configurations (SPF, DKIM, DMARC) to ensure your website and emails always resolve correctly.",
                    'quote': "DNS done right.",
                    'bullet_title': 'DNS Services',
                    'bullets': ['Domain Privacy', 'DNSSEC', 'Email Auth Records', 'Global Anycast DNS'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Peace of Mind',
             'items': [
                 '99.9% Uptime guarantee.',
                 'Automated daily backups.',
                 '24/7 Technical support.',
                 'Free SSL certificate management.'
             ]
        }
    },
    'services/cloud-migration.html': {
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png',
        'title': 'Cloud Migration',
        'intro': "Moving to the cloud doesn't have to be disruptive. We handle the entire migration lifecycle—from assessment to cutover—ensuring zero data loss and minimal downtime.",
        'services': [
            {
                'title': 'Lift and Shift', 
                'desc': 'Moving applications as-is to the cloud for quick wins.',
                'details': {
                    'long_desc': "Fast track to cloud. We migrate your existing virtual machines or applications directly to the cloud with minimal changes, allowing you to exit your data center quickly.",
                    'quote': "Quick migration.",
                    'bullet_title': 'Rehosting',
                    'bullets': ['VM Import/Export', 'Network Extension', 'Fast Cutover', 'Minimal Downtime'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Re-platforming', 
                'desc': 'Optimizing applications for cloud-native services (databases, storage).',
                'details': {
                    'long_desc': "Optimize while moving. We modify your applications slightly to take advantage of managed cloud services, like switching from a self-hosted SQL server to Amazon RDS for better manageability.",
                    'quote': "Smart optimization.",
                    'bullet_title': 'Refactoring',
                    'bullets': ['Managed Databases', 'S3 Integration', 'Auto-scaling', 'Containerization'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Database Migration', 
                'desc': 'Secure transfer of data to cloud databases (RDS, SQL Azure).',
                'details': {
                    'long_desc': "Safe data transit. We use specialized tools to migrate your databases securely, ensuring data integrity and keeping your business running with change data capture (CDC) during the move.",
                    'quote': "Secure data move.",
                    'bullet_title': 'DB Migration',
                    'bullets': ['Schema Conversion', 'Data Replication', 'Validation Checks', 'Zero Data Loss'],
                    'image': 'service_data_1770395144717.png'
                }
            },
            {
                'title': 'Post-Migration Optimization', 
                'desc': 'Tuning resources post-move for cost and performance.',
                'details': {
                    'long_desc': "Refining the new home. After migration, we continuously monitor performance and costs, right-sizing instances and implementing savings plans to ensure you get the best ROI.",
                    'quote': "Continuous tuning.",
                    'bullet_title': 'Optimization',
                    'bullets': ['Cost Analysis', 'Performance Tuning', 'Security Hardening', 'Compliance Check'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }
        ],
        'benefits': {
             'title': 'Seamless Transition',
             'items': [
                 'Minimal business disruption.',
                 'Secure data transfer.',
                 'Immediate access to cloud scalability.',
                 'Cost-effective migration planning.'
             ]
        }
    },
    'services/backup-disaster-recovery.html': {
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png',
        'title': 'Backup & Disaster Recovery',
        'intro': "Data loss can be catastrophic. We implement comprehensive backup and disaster recovery (BDR) strategies to ensure your business can bounce back from ransomware, hardware failure, or natural disasters.",
        'services': [
            {
                'title': 'Automated Cloud Backups', 
                'desc': 'Encrypted, off-site backups with retention policies.',
                'details': {
                    'long_desc': "Set and forget. We configure automated, encrypted backups of your servers and data to secure cloud storage. Retention policies ensure you can roll back to any point in time.",
                    'quote': "Data insurance.",
                    'bullet_title': 'Backup Features',
                    'bullets': ['Incrememental Backup', 'Encryption at Rest', 'Immutable Storage', 'Long-term Retention'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Disaster Recovery Planning', 
                'desc': 'Defining RTO (Recovery Time Objective) and RPO (Recovery Point Objective).',
                'details': {
                    'long_desc': "Plan for the worst. We work with you to define your business's tolerance for downtime (RTO) and data loss (RPO), and design a recovery strategy that meets those targets.",
                    'quote': "Strategic recovery.",
                    'bullet_title': 'DR metrics',
                    'bullets': ['RTO / RPO Definition', 'Business Impact Analysis', 'Call Trees', 'Recovery Runbooks'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Business Continuity Testing', 
                'desc': 'Regular drills to verify recovery procedures.',
                'details': {
                    'long_desc': "Practice makes perfect. We don't just hope it works; we perform regular DR drills to verify that we can restore your systems within the agreed timeframes.",
                    'quote': "Tested & proven.",
                    'bullet_title': 'Drills',
                    'bullets': ['Annual DR Tests', 'Tabletop Exercises', 'Restore Verification', 'Process Updates'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Failover Solutions', 
                'desc': 'Hot or warm standby systems for immediate switchover.',
                'details': {
                    'long_desc': "Instant recovery. For mission-critical systems, we set up hot standby replicas that can take over immediately if the primary system fails, ensuring near-zero downtime.",
                    'quote': "Always on.",
                    'bullet_title': 'Failover',
                    'bullets': ['Active-Passive', 'Active-Active', 'DNS Failover', 'Auto-healing'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            }
        ],
        'benefits': {
             'title': 'Business Resilience',
             'items': [
                 'Protection against ransomware.',
                 'Compliance with data protection laws.',
                 'Rapid restoration of operations.',
                 'Safeguarding business reputation.'
             ]
        }
    },
    'services/it-support-maintenance.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'IT Support & Maintenance',
        'intro': "Your outsourced IT department. We provide responsive helpdesk support and proactive maintenance to keep your employees productive and your technology frustration-free.",
        'services': [
            {
                'title': '24/7 Help Desk', 
                'desc': 'Remote and on-site support for hardware and software issues.',
                'details': {
                    'long_desc': "Help is one call away. Our friendly support technicians are available around the clock to assist your team with password resets, software errors, email issues, and more.",
                    'quote': "Always available.",
                    'bullet_title': 'Support Channels',
                    'bullets': ['Phone / Email / Chat', 'Remote Desktop', 'On-site Visits', 'Ticket Portal'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Workstation Management', 
                'desc': 'Setup, configuration, and troubleshooting for PCs and Macs.',
                'details': {
                    'long_desc': "Optimized endpoints. We manage the lifecycle of your employee computers, from initial setup and software installation to troubleshooting and eventual secure disposal.",
                    'quote': "Productive teams.",
                    'bullet_title': 'Desktop Services',
                    'bullets': ['New User Setup', 'Software Deployment', 'Antivirus Mgmt', 'Hardware Repair'],
                    'image': 'hero_office_workstation.png'
                }
            },
            {
                'title': 'Preventative Maintenance', 
                'desc': 'Regular health checks to catch issues before they cause downtime.',
                'details': {
                    'long_desc': "Proactive care. We don't wait for things to break. We run regular maintenance tasks like disk cleanup, updates, and error log reviews to keep systems healthy.",
                    'quote': "Prevent issues.",
                    'bullet_title': 'Maintenance',
                    'bullets': ['Disk Cleanup', 'OS Updates', 'Driver Updates', 'Error Log Checks'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Vendor Management', 
                'desc': 'Handling communication with your ISPs and software vendors.',
                'details': {
                    'long_desc': "One point of contact. We act as the liaison between you and your other tech vendors (internet providers, software support), saving you time and technical headaches.",
                    'quote': "We handle the tech talk.",
                    'bullet_title': 'Vendor Liaison',
                    'bullets': ['ISP Support Calls', 'Warranty Claims', 'License Renewals', 'Technical Procurement'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Focus on Business',
             'items': [
                 'Reduced IT overhead costs.',
                 'Increased employee productivity.',
                 'Predictable monthly IT spend.',
                 'Expertise on demand.'
             ]
        }
    },
    'services/remote-monitoring.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'Remote Monitoring (RMM)',
        'intro': "We watch your systems so you don't have to. Our Remote Monitoring and Management (RMM) tools track the health of your entire IT estate in real-time, alerting us to anomalies instantly.",
        'services': [
            {
                'title': 'Asset Tracking', 
                'desc': 'Real-time inventory of all hardware and software assets.',
                'details': {
                    'long_desc': "Know what you have. Our RMM agent automatically discovers and catalogs every device on your network, giving you an always-up-to-date inventory of hardware specifications and installed software.",
                    'quote': "Complete visibility.",
                    'bullet_title': 'Inventory',
                    'bullets': ['Hardware Specs', 'Installed Software', 'Warranty Status', 'Network Discovery'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Performance Alerting', 
                'desc': 'Notifications for high CPU, low disk space, or network bottlenecks.',
                'details': {
                    'long_desc': "Early warning system. We set thresholds for key performance indicators. If a server's disk gets full or CPU spikes, we get an alert instantly and can investigate before it crashes.",
                    'quote': "Instant alerts.",
                    'bullet_title': 'Metrics',
                    'bullets': ['CPU & RAM Usage', 'Disk Space', 'Offline Status', 'Service Failures'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            },
            {
                'title': 'Automated Scripting', 
                'desc': 'Self-healing scripts to fix common issues automatically.',
                'details': {
                    'long_desc': "Auto-healing. We deploy automation scripts that can automatically restart stuck services, clear temporary files, or reboot frozen applications without human intervention.",
                    'quote': "Self-healing IT.",
                    'bullet_title': 'Automation',
                    'bullets': ['Service Restarts', 'Temp File Cleanup', 'Auto-remediation', 'Scheduled Tasks'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Reporting', 
                'desc': 'Detailed monthly reports on system health and uptime.',
                'details': {
                    'long_desc': "Transparency. You get executive-level reports every month showing the health of your environment, patches applied, threats blocked, and overall uptime metrics.",
                    'quote': "Clear insights.",
                    'bullet_title': 'Reports',
                    'bullets': ['Executive Summary', 'Asset Health', 'Patch Compliance', 'Ticket History'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Proactive Care',
             'items': [
                 'Resolve issues before they impact users.',
                 'Data-driven capacity planning.',
                 'Complete visibility into IT assets.',
                 'Enhanced security posture.'
             ]
        }
    },
    'services/patch-management.html': {
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png',
        'title': 'Patch Management',
        'intro': "Unpatched software is a security risk. We automate the patching process for Operating Systems and third-party applications, closing security loopholes and ensuring stability.",
        'services': [
            {
                'title': 'OS Updates', 
                'desc': 'Testing and deploying Windows, macOS, and Linux updates.',
                'details': {
                    'long_desc': "Secure the core. We test and deploy security updates and feature packs for Windows, macOS, and Linux, ensuring your operating systems are hardened against known exploits.",
                    'quote': "Hardened OS.",
                    'bullet_title': 'OS Patching',
                    'bullets': ['Feature Updates', 'Security Rollups', 'Driver Updates', 'Reboot Management'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Third-Party Patching', 
                'desc': 'Updates for Chrome, Adobe, Java, and other critical apps.',
                'details': {
                    'long_desc': "Update everything. It's not just Windows. We update common business applications like Chrome, Adobe Reader, Zoom, and Java, which are often targets for attackers.",
                    'quote': "App security.",
                    'bullet_title': '3rd Party Apps',
                    'bullets': ['Browsers', 'Office / PDF Tools', 'Runtimes (Java/Go)', 'Collaboration Tools'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Compliance Reporting', 
                'desc': 'Proof of patch status for auditors and regulators.',
                'details': {
                    'long_desc': "Audit ready. We track every patch deployed to every machine. If you have compliance requirements (HIPAA, GDPR), we provide the reports proving your systems are up to date.",
                    'quote': "Prove compliance.",
                    'bullet_title': 'Compliance',
                    'bullets': ['Patch Audits', 'Vulnerability Reports', 'CVE Tracking', 'Historical Data'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Scheduling', 
                'desc': 'Applying patches during off-hours to minimize disruption.',
                'details': {
                    'long_desc': "Zero interruption. We schedule patching windows during nights or weekends so your employees aren't interrupted by sudden reboots or \"Applying Updates\" screens during the workday.",
                    'quote': "Patching while you sleep.",
                    'bullet_title': 'Windows',
                    'bullets': ['Maintenance Windows', 'Wake-on-LAN', 'User Deferrals', 'Post-patch Checks'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Security & Compliance',
             'items': [
                 'Protection against known vulnerabilities.',
                 'System stability improvements.',
                 'Compliance with security standards (ISO, PCI-DSS).',
                 'Automated, worry-free maintenance.'
             ]
        }
    },
    'services/security-assessments.html': {
        'hero_image': 'hero_cybersecurity_shield_1770688439064.png',
        'title': 'Security Assessments',
        'intro': "You can't secure what you don't know exists. We perform rigorous vulnerability assessments and penetration testing to identify weaknesses in your defenses before attackers do.",
        'services': [
            {
                'title': 'Vulnerability Scanning', 
                'desc': 'Automated scans to find outdated software and misconfigurations.',
                'details': {
                    'long_desc': "Find the gaps. We run automated scanners against your network and web applications to identify known vulnerabilities, missing patches, and weak configurations.",
                    'quote': "Identify risks.",
                    'bullet_title': 'Scanning',
                    'bullets': ['Network Scans', 'Web App Scans', 'Credential Checks', 'Port Scanning'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Penetration Testing', 
                'desc': 'Ethical hacking to simulate real-world attacks on your apps and network.',
                'details': {
                    'long_desc': "Simulate the enemy. Our certified ethical hackers attempt to exploit vulnerabilities in your systems (with your permission) to see how deep an attacker could get and what data is at risk.",
                    'quote': "Ethical hacking.",
                    'bullet_title': 'PenTest',
                    'bullets': ['External/Internal', 'Web/Mobile Apps', 'Social Engineering', 'Exploitation'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Security Audits', 
                'desc': 'Reviewing policies and controls against best practices.',
                'details': {
                    'long_desc': "Policy review. We examine your security policies, user access controls, and administrative procedures, comparing them against industry frameworks like NIST or ISO 27001.",
                    'quote': "Best practices.",
                    'bullet_title': 'Audit Scope',
                    'bullets': ['Access Controls', 'Policy Review', 'Physical Security', 'Configuration Review'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'Phishing Simulation', 
                'desc': 'Testing employee awareness against social engineering attacks.',
                'details': {
                    'long_desc': "Test the human firewall. We send safe, simulated phishing emails to your employees to see who clicks, and then provide targeted training to those who need it.",
                    'quote': "Security awareness.",
                    'bullet_title': 'Phishing',
                    'bullets': ['Simulated Campaigns', 'Click Tracking', 'Educational Moments', 'Trend Analysis'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Identify & Remediate',
             'items': [
                 'Clear roadmap for security improvements.',
                 'Verification of existing controls.',
                 'Compliance with data protection regulations.',
                 'Reduced risk of data breaches.'
             ]
        }
    },
    'services/firewall-endpoint-protection.html': {
        'hero_image': 'hero_cybersecurity_shield_1770688439064.png',
        'title': 'Firewall & Endpoint Protection',
        'intro': "Secure the perimeter and the devices. We deploy Next-Generation Firewalls (NGFW) and advanced Endpoint Detection and Response (EDR) solutions to block threats at every entry point.",
        'services': [
            {
                'title': 'Next-Gen Firewall Setup', 
                'desc': 'Deep packet inspection, intrusion prevention, and web filtering.',
                'details': {
                    'long_desc': "The castle walls. We deploy intelligent firewalls that go beyond simple port blocking. They inspect traffic content, block malware, filter malicious websites, and detect intrusion attempts.",
                    'quote': "Intelligent defense.",
                    'bullet_title': 'NGFW Features',
                    'bullets': ['App Awareness', 'IPS/IDS', 'Content Filtering', 'SSL Inspection'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Endpoint Protection (EDR)', 
                'desc': ' AI-driven anti-malware that stops ransomware and zero-day threats.',
                'details': {
                    'long_desc': "Stop threats at the device. Legacy antivirus isn't enough. We deploy EDR agents that use AI and behavioral analysis to stop ransomware and zero-day attacks even if they've never been seen before.",
                    'quote': "Stop ransomware.",
                    'bullet_title': 'EDR',
                    'bullets': ['Behavioral Analysis', 'Ransomware Rollback', 'Device Isolation', 'Threat Hunting'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'VPN Configuration', 
                'desc': 'Secure remote access for your distributed workforce.',
                'details': {
                    'long_desc': "Work from anywhere, securely. We configure Client VPNs with strong encryption and Multi-Factor Authentication, ensuring your remote staff can access office resources safely.",
                    'quote': "Secure remote work.",
                    'bullet_title': 'VPN',
                    'bullets': ['SSL VPN', 'MFA Integration', 'Split Tunneling', 'Device Checks'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            },
            {
                'title': 'Mobile Device Management (MDM)', 
                'desc': 'Securing corporate data on employee smartphones.',
                'details': {
                    'long_desc': "Secure the small screens. We implement MDM to secure email and documents on employee phones, allowing for remote wipe of corporate data if a device is lost or the employee leaves.",
                    'quote': "Mobile security.",
                    'bullet_title': 'MDM',
                    'bullets': ['Enforce Passcodes', 'Separate Work/Personal', 'Remote Wipe', 'App Deployment'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ],
        'benefits': {
             'title': 'Comprehensive Defense',
             'items': [
                 'Real-time threat blocking.',
                 'Visibility into network traffic.',
                 'Protection for remote workers.',
                 'Rapid containment of infected devices.'
             ]
        }
    },
    'services/identity-access-mgmt.html': {
        'hero_image': 'hero_cybersecurity_shield_1770688439064.png',
        'title': 'Identity Access Mgmt (IAM)',
        'intro': "Identity is the new perimeter. We implement robust Identity and Access Management (IAM) solutions to ensure that the right people have the right access to the right resources.",
        'services': [
            {
                'title': 'Multi-Factor Authentication (MFA)', 
                'desc': 'Adding a critical layer of security to all logins.',
                'details': {
                    'long_desc': "The single best security upgrade. We enable MFA everywhere—email, VPNs, cloud apps. Even if a password is stolen, the attacker can't get in without the second factor.",
                    'quote': "Verify requests.",
                    'bullet_title': 'MFA Options',
                    'bullets': ['Push Notifications', 'Authenticator Apps', 'Hardware Keys', 'Biometrics'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            },
            {
                'title': 'Single Sign-On (SSO)', 
                'desc': 'One secure credential for all your applications.',
                'details': {
                    'long_desc': "One key, many doors. We integrate your apps with an SSO provider (like Okta or Azure AD). Users log in once and get access to everything, reducing password fatigue and Help Desk tickets.",
                    'quote': "Seamless access.",
                    'bullet_title': 'SSO Benefits',
                    'bullets': ['Better User Exp', 'Centralized Access', 'Fewer Passwords', 'Easy Onboarding'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Privileged Access Management (PAM)', 
                'desc': 'Securing and monitoring admin accounts.',
                'details': {
                    'long_desc': "Guard the keys to the kingdom. We implement PAM to tightly control, monitor, and record the use of administrator accounts, ensuring they are only used when authorized.",
                    'quote': "Admin security.",
                    'bullet_title': 'PAM',
                    'bullets': ['Just-in-Time Access', 'Session Recording', 'Password Rotation', 'Approval Workflows'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            },
            {
                'title': 'User Lifecycle Management', 
                'desc': 'Automating onboarding and offboarding access rights.',
                'details': {
                    'long_desc': "Automated access. When HR hires someone, their accounts are created automatically. When they leave, access is revoked instantly everywhere, closing security gaps.",
                    'quote': "Automated lifecycle.",
                    'bullet_title': 'Lifecycle',
                    'bullets': ['HR Integration', 'Role-Based Access', 'Instant Revocation', 'Access Reviews'],
                    'image': 'hero_office_workstation.png'
                }
            }
        ],
        'benefits': {
             'title': 'Zero Trust Security',
             'items': [
                 'Prevention of credential theft attacks.',
                 'Improved user experience (SSO).',
                 'Granular control over data access.',
                 'simplified compliance auditing.'
             ]
        }
    },

    # --- New Pages for Menu Expansion ---
    'services/ui-ux-design.html': {
        'hero_image': 'hero_marketing_creative_1770688454386.png',
        'title': 'UI/UX Design',
        'intro': "User Interface and User Experience design are at the heart of digital products. We create intuitive, engaging, and aesthetically pleasing designs that delight users and drive conversions.",
        'services': [
            {
                'title': 'User Research', 
                'desc': 'Understanding user behaviors, needs, and motivations.',
                'details': {
                    'long_desc': "Design starts with people. We conduct in-depth user research through interviews, surveys, and usability testing to understand your audience's needs, pain points, and motivations.",
                    'quote': "Empathy first.",
                    'bullet_title': 'Research Methods',
                    'bullets': ['User Interviews', 'Personas & Scenarios', 'Competitor Analysis', 'User Journey Mapping'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Wireframing & Prototyping', 
                'desc': 'Visualizing the structure and flow of the interface.',
                'details': {
                    'long_desc': "Blueprints for success. We create low-fidelity wireframes to establish the structure and flow, followed by high-fidelity interactive prototypes to validate the concept before expensive development begins.",
                    'quote': "Fail fast, learn faster.",
                    'bullet_title': 'Prototyping',
                    'bullets': ['Information Architecture', 'Low-Fi Wireframes', 'Interactive Prototypes', 'Click-through Models'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Visual Design', 
                'desc': 'Creating pixel-perfect high-fidelity mockups.',
                'details': {
                    'long_desc': "Pixel perfection. We apply color, typography, and imagery to bring the product to life, creating a visually stunning interface that aligns with your brand identity.",
                    'quote': "Beautiful interfaces.",
                    'bullet_title': 'UI Elements',
                    'bullets': ['Design Systems', 'Iconography', 'Typography', 'Color Theory'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Usability Testing', 
                'desc': 'Validating designs with real users to ensure ease of use.',
                'details': {
                    'long_desc': "Proven to work. We test our designs with real users to identify friction points and confusion, iterating on the interface until it is intuitive and easy to use.",
                    'quote': "User validated.",
                    'bullet_title': 'Testing',
                    'bullets': ['A/B Testing', 'Eye Tracking', 'Heuristic Evaluation', 'Accessibility Audit'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ],
        'benefits': { 'title': 'Design that Works', 'items': ['Higher user satisfaction.', 'Increased conversion rates.', 'Reduced development rework.', 'Stronger brand perception.']}
    },
    'services/logo-design.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'Logo Design', 
        'intro': "Your logo is the face of your brand. We design memorable, versatile, and timeless logos that communicate your brand's essence in a single glance.", 
        'services': [
            {
                'title': 'Concept Development', 
                'desc': 'Brainstorming unique visual metaphors.',
                'details': {
                    'long_desc': "The big idea. We explore dozens of concepts and visual metaphors that represent your brand's values, mission, and personality, narrowing them down to the strongest contenders.",
                    'quote': "Visual storytelling.",
                    'bullet_title': 'Concepts',
                    'bullets': ['Mind Mapping', 'Sketching', 'Visual Metaphors', 'Mood Boards'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            },
            {
                'title': 'Typography Selection', 
                'desc': 'Choosing the right fonts to match your tone.',
                'details': {
                    'long_desc': "Type matters. The font you use says as much as the words themselves. We carefully select or create custom typography that complements your symbol and conveys the right tone.",
                    'quote': "Words as art.",
                    'bullet_title': 'Typography',
                    'bullets': ['Serif vs Sans', 'Custom Lettering', 'Kerning & Tracking', 'Font Pairing'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            },
            {
                'title': 'Brand Marks', 
                'desc': 'Creating iconic symbols.',
                'details': {
                    'long_desc': "Iconic simplicity. We design unique graphic symbols or logomarks that can stand alone or work alongside your company name, perfect for social media avatars and app icons.",
                    'quote': "Instant recognition.",
                    'bullet_title': 'Marks',
                    'bullets': ['Abstract Marks', 'Pictorial Marks', 'Monograms', 'Mascots'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            },
            {
                'title': 'Brand Guidelines', 
                'desc': 'Defining usage rules for consistency.',
                'details': {
                    'long_desc': "The rulebook. We deliver a comprehensive brand style guide detailing how to use your logo, fonts, colors, and imagery to ensure consistency across all touchpoints.",
                    'quote': "Consistent identity.",
                    'bullet_title': 'Guidelines',
                    'bullets': ['Logo Usage', 'Color Palette', 'Typography Rules', 'Dos and Donts'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Memorable Identity', 'items': ['Instant brand recognition.', 'Professional appeal.', 'Versatility across media.', 'Timeless design.']} 
    },
    'services/brochure-design.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'Brochure Design', 
        'intro': "Print media still has a powerful place in marketing. We design professional brochures, flyers, and catalogs that leave a lasting physical impression on your clients.", 
        'services': [
            {
                'title': 'Layout Design', 
                'desc': 'Organizing information for readability and impact.',
                'details': {
                    'long_desc': "Guided reading. We structure your content with a clear hierarchy, using grids, whitespace, and imagery to guide the reader's eye through the most important information.",
                    'quote': "Structured impact.",
                    'bullet_title': 'Layout',
                    'bullets': ['Grid Systems', 'Visual Hierarchy', 'Whitespace Usage', 'Focal Points'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Copywriting', 
                'desc': 'Crafting compelling messages.',
                'details': {
                    'long_desc': "Words that sell. Our copywriters craft persuasive headlines and body text that clearly communicate your value proposition and drive the reader to take action.",
                    'quote': "Persuasive text.",
                    'bullet_title': 'Copy',
                    'bullets': ['Headlines', 'Benefits vs Features', 'Call to Action', 'Tone of Voice'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Print Production', 
                'desc': 'Preparing files for high-quality printing.',
                'details': {
                    'long_desc': "Ready for press. We handle the technical side of print design, ensuring correct color modes (CMYK), bleed areas, and high-resolution images for a flawless final product.",
                    'quote': "Print perfect.",
                    'bullet_title': 'Production',
                    'bullets': ['CMYK Color', 'Bleed & Trim', 'Paper Selection', 'Die Cuts'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Digital Brochures', 
                'desc': 'Interactive PDFs for online distribution.',
                'details': {
                    'long_desc': "Go digital. We create interactive PDF versions of your brochures with clickable links, embedded videos, and navigation menus for email distribution and website download.",
                    'quote': "Interactive docs.",
                    'bullet_title': 'Digital Features',
                    'bullets': ['Hyperlinks', 'Navigation Tabs', 'Embedded Media', 'Form Fields'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Tangible Impact', 'items': ['High-quality tactile experience.', 'Effective sales collateral.', 'Information retention.', 'Professional presentation.']} 
    },
    'services/website-design-dubai.html': { 
        'hero_image': 'hero_web_dev_futuristic_1770688377502.png', 
        'title': 'Website Design Dubai', 
        'intro': "Located in the heart of innovation, we deliver world-class website designs for Dubai-based businesses. We understand the local market nuances and global design standards.", 
        'services': [
            {
                'title': 'Localized Design', 
                'desc': 'Culturally relevant aesthetics for the UAE market.',
                'details': {
                    'long_desc': "Local relevance. We understand the aesthetic preferences and cultural nuances of the Dubai and GCC market, creating designs that resonate with local audiences while maintaining global appeal.",
                    'quote': "Culturally tuned.",
                    'bullet_title': 'Localization',
                    'bullets': ['Cultural Aesthetics', 'Local Imagery', 'Color symbolism', 'Market Trends'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Bilingual Interfaces', 
                'desc': 'Seamless English and Arabic user experiences.',
                'details': {
                    'long_desc': "English & Arabic. We specialize in designing bilingual websites with full Right-to-Left (RTL) support for Arabic, ensuring the layout and typography look perfect in both languages.",
                    'quote': "Fluent design.",
                    'bullet_title': 'Bilingual',
                    'bullets': ['RTL Layouts', 'Arabic Typography', 'Language Switchers', 'Content Mirroring'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Luxury Web Design', 
                'desc': 'Premium layouts for high-end brands.',
                'details': {
                    'long_desc': "Dubai luxury. For premium brands in real estate, hospitality, and retail, we create minimalist, elegant, and high-end digital experiences that reflect exclusivity and quality.",
                    'quote': "Digital luxury.",
                    'bullet_title': 'Premium Style',
                    'bullets': ['Minimalism', 'Elegant Typography', 'High-end Imagery', 'Micro-interactions'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Responsive Development', 
                'desc': 'Mobile-first designs for a smartphone-savvy region.',
                'details': {
                    'long_desc': "Mobile first. With high smartphone penetration in the region, we ensure your website works flawlessly on all devices, from the latest iPhone to large desktop monitors.",
                    'quote': "Any device.",
                    'bullet_title': 'Responsive',
                    'bullets': ['Mobile-First', 'Tablet Adapted', 'Touch Friendly', 'Fast Loading'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Regional Expertise', 'items': ['Cultural resonance.', 'Compliance with local regulations.', 'Bilingual support (RTL).', 'High-end aesthetic standards.']} 
    },
    'services/social-media-creatives.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'Social Media Creatives', 
        'intro': "Stop the scroll. We design eye-catching social media assets for Instagram, LinkedIn, Twitter, and Facebook that engage your audience and amplify your brand message.", 
        'services': [
            {
                'title': 'Post Design', 
                'desc': 'Static images and carousels.',
                'details': {
                    'long_desc': "Feed aesthetics. We design single image posts and swipeable carousels that are visually consistent with your brand and optimized for engagement algorithms.",
                    'quote': "Scroll stoppers.",
                    'bullet_title': 'Posts',
                    'bullets': ['Instagram Carousels', 'LinkedIn Slides', 'Twitter Cards', 'Facebook Posts'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Story & Reels', 
                'desc': 'Vertical video and animated graphics.',
                'details': {
                    'long_desc': "Vertical focus. We create engaging vertical content for Stories, Reels, and TikTok, using animation and video to capture attention in the first 3 seconds.",
                    'quote': "Vertical impact.",
                    'bullet_title': 'Vertical Format',
                    'bullets': ['Animated Stories', 'Reels Editing', 'TikTok Trends', 'Highlights Covers'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Ad Creatives', 
                'desc': 'High-conversion visuals for paid campaigns.',
                'details': {
                    'long_desc': "Performance intent. We design ad creatives specifically built to convert, testing different hook images, text overlays, and calls to action to lower your CPA.",
                    'quote': "Ads that convert.",
                    'bullet_title': 'Ads',
                    'bullets': ['Facebook Ads', 'Instagram Story Ads', 'LinkedIn Sponsored', 'A/B Test Variations'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'template Design', 
                'desc': 'Reusable branding templates for your team.',
                'details': {
                    'long_desc': "DIY consistency. We create editable Canva or Photoshop templates for your in-house team, ensuring that even quick daily updates look on-brand and professional.",
                    'quote': "Brand consistency.",
                    'bullet_title': 'Templates',
                    'bullets': ['Canva Templates', 'PSD Files', 'Brand Kit', 'Font & Color Setup'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Evaluate Engagement', 'items': ['Higher click-through rates.', 'Consistent brand voice.', 'Increased shareability.', 'Professional social presence.']} 
    },
    
    'services/azure-services.html': { 
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png', 
        'title': 'Microsoft Azure Services', 
        'intro': "Unlocking the power of Microsoft Azure. We provide end-to-end consulting, migration, and management services to help you leverage Azure's vast ecosystem of cloud tools.", 
        'services': [
            {
                'title': 'Azure Migration', 
                'desc': 'Moving workloads to Azure Virtual Machines.',
                'details': {
                    'long_desc': "Move to Microsoft's cloud. We assess, plan, and execute the migration of your on-premise servers to Azure VMs or Azure App Service, minimizing downtime and optimizing for cost.",
                    'quote': "Smooth migration.",
                    'bullet_title': 'Migration',
                    'bullets': ['Assessment', 'Lift & Shift', 'Refactoring', 'Azure Migrate Tool'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }, 
            {
                'title': 'Azure AD Integration', 
                'desc': 'Unified identity management.',
                'details': {
                    'long_desc': "Identity backbone. We configure Azure Active Directory (Entra ID) to manage user identities, enabling Single Sign-On (SSO) and Multi-Factor Authentication (MFA) across your organization.",
                    'quote': "Secure identity.",
                    'bullet_title': 'Identity',
                    'bullets': ['Entra ID (Azure AD)', 'SSO Setup', 'MFA Enforcement', 'Conditional Access'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }, 
            {
                'title': 'Azure DevOps', 
                'desc': 'CI/CD pipelines on Microsoft stack.',
                'details': {
                    'long_desc': "Automate delivery. We set up Azure DevOps pipelines to automate the building, testing, and deployment of your code, ensuring faster and more reliable software releases.",
                    'quote': "DevOps automation.",
                    'bullet_title': 'DevOps',
                    'bullets': ['CI/CD Pipelines', 'Azure Repos', 'Board Management', 'Artifacts'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Azure SQL', 
                'desc': 'Managed database services.',
                'details': {
                    'long_desc': "Managed data. We migrate and optimize your databases on Azure SQL Database, taking advantage of built-in high availability, backups, and AI-powered performance tuning.",
                    'quote': "Intelligent SQL.",
                    'bullet_title': 'Data',
                    'bullets': ['Azure SQL', 'Cosmos DB', 'Data Factory', 'Synapse Analytics'],
                    'image': 'service_data_1770395144717.png'
                }
            }
        ], 
        'benefits': {'title': 'Enterprise Grade', 'items': ['Seamless Windows integration.', 'Enterprise-grade security.', 'Global data center availability.', 'Hybrid cloud capabilities.']} 
    },
    'services/aws-services.html': { 
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png', 
        'title': 'AWS Cloud Services', 
        'intro': "Build on the world's most adopted cloud. We are AWS experts helping you architect, secure, and scale your applications on Amazon Web Services.", 
        'services': [
            {
                'title': 'EC2 & Lambda', 
                'desc': 'Compute and serverless solutions.',
                'details': {
                    'long_desc': "Compute power. Whether you need scalable virtual servers (EC2) or event-driving serverless functions (Lambda), we architect the right compute layer for your application needs.",
                    'quote': "Scalable compute.",
                    'bullet_title': 'Compute',
                    'bullets': ['EC2 Instances', 'AWS Lambda', 'Auto Scaling', 'Elastic Beanstalk'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }, 
            {
                'title': 'S3 & Storage', 
                'desc': 'Scalable object storage.',
                'details': {
                    'long_desc': "Infinite storage. We configure Amazon S3 for secure, durable, and low-cost object storage, along with EBS for high-performance block storage attached to your instances.",
                    'quote': "Reliable storage.",
                    'bullet_title': 'Storage',
                    'bullets': ['S3 Buckets', 'EBS Volumes', 'Glacier Archiving', 'Storage Gateway'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            }, 
            {
                'title': 'AWS Security', 
                'desc': 'IAM and VPC configuration.',
                'details': {
                    'long_desc': "Security first. We design secure VPC network architectures and granular IAM policies to ensure your AWS environment follows the Principle of Least Privilege.",
                    'quote': "Cloud security.",
                    'bullet_title': 'Security',
                    'bullets': ['IAM Policies', 'VPC Design', 'Security Groups', 'WAF & Shield'],
                    'image': 'hero_cybersecurity_shield_1770688439064.png'
                }
            }, 
            {
                'title': 'Cost Optimization', 
                'desc': 'Managing AWS spend effectively.',
                'details': {
                    'long_desc': "Control costs. We analyze your AWS usage and implement cost-saving strategies like Reserved Instances, Savings Plans, and rightsizing to keep your cloud bill in check.",
                    'quote': "Efficient spend.",
                    'bullet_title': 'Cost Ops',
                    'bullets': ['Cost Explorer', 'Budgets & Alerts', 'Reserved Instances', 'Spot Instances'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }
        ], 
        'benefits': {'title': 'Market Leader', 'items': ['Extensive service catalog.', 'Unmatched scalability.', 'Global reach.', 'Mature ecosystem.']} 
    },
    'services/gcp-services.html': { 
        'hero_image': 'hero_cloud_computing_ethereal_1770688425145.png', 
        'title': 'Google Cloud (GCP)', 
        'intro': "Innovate with Google's technology. We help you harness Google Cloud Platform for its superior data analytics, AI/ML capabilities, and container orchestration.", 
        'services': [
            {
                'title': 'BigQuery Analytics', 
                'desc': 'Serverless data warehousing.',
                'details': {
                    'long_desc': "Analyze everything. We set up BigQuery to process petabytes of data in seconds, giving you real-time insights into your business without the headache of managing infrastructure.",
                    'quote': "Data at scale.",
                    'bullet_title': 'Data',
                    'bullets': ['BigQuery', 'Dataflow', 'Looker Studio', 'Pub/Sub'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }, 
            {
                'title': 'GKE (Kubernetes)', 
                'desc': 'Managed Kubernetes environment.',
                'details': {
                    'long_desc': "Standard for containers. We deploy and manage your containerized applications on Google Kubernetes Engine (GKE), the industry standard for container orchestration, built by Google.",
                    'quote': "K8s experts.",
                    'bullet_title': 'Containers',
                    'bullets': ['GKE Clusters', 'Container Registry', 'Autopilot Mode', 'Anthos'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Cloud Functions', 
                'desc': 'Event-driven serverless code.',
                'details': {
                    'long_desc': "Code without servers. We write and deploy single-purpose functions that scale automatically in response to events, perfect for lightweight APIs and background processing.",
                    'quote': "Pure code.",
                    'bullet_title': 'Serverless',
                    'bullets': ['Cloud Functions', 'Cloud Run', 'Eventarc', 'Firebase'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }, 
            {
                'title': 'AI Platform', 
                'desc': 'Training and deploying ML models.',
                'details': {
                    'long_desc': "Machine learning made easy. We utilize Vertex AI and Google's pre-trained models to add intelligence to your apps, from vision and speech to advanced predictive analytics.",
                    'quote': "AI powered.",
                    'bullet_title': 'AI/ML',
                    'bullets': ['Vertex AI', 'AutoML', 'TensorFlow', 'Vision API'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }
        ], 
        'benefits': {'title': 'Data & AI First', 'items': ['Best-in-class data analytics.', 'Global fiber network.', 'Kubernetes leadership.', 'Sustainable infrastructure.']} 
    },
    
    'services/seo-optimization.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'SEO Optimization', 
        'intro': "Be found by the right people. Our SEO strategies improve your visibility on search engines, driving organic traffic that sustains your business long-term.", 
        'services': [
            {
                'title': 'Technical SEO', 
                'desc': 'Optimizing site structure and speed.',
                'details': {
                    'long_desc': "Optimization under the hood. We fix crawl errors, improve site speed, ensure mobile-friendliness, and implement structured data to help search engines understand and rank your site.",
                    'quote': "Crawlable & fast.",
                    'bullet_title': 'Technical',
                    'bullets': ['Site Speed', 'XML Sitemaps', 'Schema Markup', 'Mobile Usability'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Keyword Research', 
                'desc': 'Targeting high-intent search terms.',
                'details': {
                    'long_desc': "Targeting intent. We identify the exact phrases your potential customers are searching for, prioritizing keywords with high commercial intent and achievable competition levels.",
                    'quote': "Search intent.",
                    'bullet_title': 'Keywords',
                    'bullets': ['Volume Analysis', 'Competition Check', 'Long-tail Keywords', 'User Intent'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'On-Page SEO', 
                'desc': 'Content and metadata optimization.',
                'details': {
                    'long_desc': "Content optimization. We optimize your titles, meta descriptions, headings, and body content to align with target keywords while keeping the copy engaging for human readers.",
                    'quote': "Optimized content.",
                    'bullet_title': 'On-Page',
                    'bullets': ['Title Tags', 'Meta Descriptions', 'Heading Tags (H1-H6)', 'Internal Linking'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Link Building', 
                'desc': 'Building authority through backlinks.',
                'details': {
                    'long_desc': "Authority building. We execute white-hat link building strategies to earn high-quality backlinks from reputable sites in your industry, signaling trust to search engines.",
                    'quote': "Domain authority.",
                    'bullet_title': 'Off-Page',
                    'bullets': ['Guest Posting', 'Digital PR', 'Local Citations', 'Competitor Links'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Organic Growth', 'items': ['Sustainable traffic.', 'Cost-effective leads.', 'Brand authority.', 'Higher ROI than ads.']} 
    },
    'services/geo-optimization.html': { 
        'hero_image': 'hero_emerging_tech_ai_1770688470055.png', 
        'title': 'GEO - Generative Engine Optimization', 
        'intro': "Optimize for AI-powered search. As ChatGPT, Perplexity, and other generative engines reshape how people find information, we ensure your brand appears prominently in AI-generated responses.", 
        'services': [
            {
                'title': 'AI Content Indexing', 
                'desc': 'Structuring content for AI comprehension.',
                'details': {
                    'long_desc': "AI-first content. We optimize your content structure, metadata, and semantic markup to ensure generative AI models can accurately understand, cite, and recommend your brand in their responses.",
                    'quote': "AI-readable content.",
                    'bullet_title': 'Indexing',
                    'bullets': ['Semantic HTML', 'Schema.org Markup', 'Entity Recognition', 'Knowledge Graphs'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }, 
            {
                'title': 'Citation Authority', 
                'desc': 'Building credible reference signals.',
                'details': {
                    'long_desc': "Become the source. We establish your content as an authoritative reference through strategic partnerships, high-quality backlinks, and verified credentials that AI engines prioritize when citing sources.",
                    'quote': "Trusted authority.",
                    'bullet_title': 'Authority',
                    'bullets': ['E-E-A-T Signals', 'Author Credentials', 'Verified Sources', 'Industry Recognition'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Conversational Keywords', 
                'desc': 'Targeting natural language queries.',
                'details': {
                    'long_desc': "Natural queries. We optimize for how people actually ask questions to AI assistants—conversational, long-form queries that differ from traditional search keywords.",
                    'quote': "Natural language.",
                    'bullet_title': 'Queries',
                    'bullets': ['Question-based Content', 'Long-tail Phrases', 'Intent Mapping', 'Answer Snippets'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Multimodal Optimization', 
                'desc': 'Optimizing text, images, and video for AI.',
                'details': {
                    'long_desc': "Multi-format visibility. We optimize all content formats—text, images, videos, and audio—so generative engines can reference your brand across visual, voice, and text-based queries.",
                    'quote': "Omnichannel AI.",
                    'bullet_title': 'Multimodal',
                    'bullets': ['Alt Text \u0026 Captions', 'Video Transcripts', 'Audio Metadata', 'Image SEO'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }
        ], 
        'benefits': {'title': 'Future-Proof Visibility', 'items': ['AI citation presence.', 'Conversational discovery.', 'Multi-platform reach.', 'Early mover advantage.']} 
    },
    'services/ppc-management.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'PPC Management', 
        'intro': "Instant targeted traffic. We manage your Google Ads and social media campaigns to maximize every dollar of your ad spend.", 
        'services': [
            {
                'title': 'Campaign Strategy', 
                'desc': 'Defining goals and audiences.',
                'details': {
                    'long_desc': "Strategic goals. We define clear KPIs for your campaigns, whether it's lead generation or e-commerce sales, and select the right platforms and ad formats to achieve them.",
                    'quote': "Targeted goals.",
                    'bullet_title': 'Strategy',
                    'bullets': ['Goal Setting', 'Audience Targeting', 'Platform Selection', 'Bidding Strategy'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Ad Copywriting', 
                'desc': 'Compelling text that drives clicks.',
                'details': {
                    'long_desc': "Click-worthy copy. We write persuasive ad headlines and descriptions that highlight your unique selling proposition and include strong calls to action.",
                    'quote': "High CTR.",
                    'bullet_title': 'Creative',
                    'bullets': ['Headlines', 'Descriptions', 'Ad Extensions', 'A/B Testing'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Bid Management', 
                'desc': 'Optimizing costs per click.',
                'details': {
                    'long_desc': "Smart bidding. We monitor and adjust bids daily to ensure you're getting the most clicks for your budget, lowering your average Cost Per Click (CPC) over time.",
                    'quote': "Budget efficiency.",
                    'bullet_title': 'Bidding',
                    'bullets': ['Manual Bidding', 'Automated Strategies', 'Budget Allocation', 'Negative Keywords'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Performance Reporting', 
                'desc': 'Transparent ROI analysis.',
                'details': {
                    'long_desc': "Total transparency. We provide detailed reports showing exactly where your money went and what you got in return—clicks, conversions, and cost per acquisition.",
                    'quote': "Clear ROI.",
                    'bullet_title': 'Reporting',
                    'bullets': ['Conversion Tracking', 'Cost Per Lead', 'ROAS Calculation', 'Monthly Reports'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Immediate Results', 'items': ['Instant visibility.', 'Precise targeting.', 'Flexible budgeting.', 'Measurable outcomes.']} 
    },
    'services/video-animation.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'Video & Animation', 
        'intro': "Motion captures attention. We create engaging explainer videos, 2D/3D animations, and promotional clips that tell your story dynamically.", 
        'services': [
            {
                'title': 'Explainer Videos', 
                'desc': 'Simplifying complex concepts.',
                'details': {
                    'long_desc': "Simplify the complex. We create 60-90 second animated videos that break down complex products or services into easy-to-understand visual stories.",
                    'quote': "Visual learning.",
                    'bullet_title': 'Explainers',
                    'bullets': ['Scriptwriting', 'Storyboard', 'Voiceover', '2D Animation'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': '3D Product Animation', 
                'desc': 'Showcasing products in detail.',
                'details': {
                    'long_desc': "3D Realism. We create photo-realistic 3D animations of your physical products, allowing customers to see features and internal mechanisms that photography can't capture.",
                    'quote': "Product showcase.",
                    'bullet_title': '3D Anim',
                    'bullets': ['Modeling', 'Texturing', 'Lighting', 'Rendering'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Motion Graphics', 
                'desc': 'Animated UI and branding.',
                'details': {
                    'long_desc': "Brand in motion. We add life to your branding with animated logos, kinetic typography, and UI animations that give your digital presence a premium feel.",
                    'quote': "Dynamic brand.",
                    'bullet_title': 'Motion',
                    'bullets': ['Logo Reveals', 'Kinetic Type', 'UI Transitions', 'Social Assets'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Video Editing', 
                'desc': 'Professional post-production.',
                'details': {
                    'long_desc': "Polished footage. We edit your raw footage into professional promotional videos, adding color grading, sound design, and special effects.",
                    'quote': "Pro cut.",
                    'bullet_title': 'Post-Prod',
                    'bullets': ['Cutting', 'Color Grading', 'Sound Design', 'VFX'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Engage & Convert', 'items': ['Higher engagement rates.', 'Better information retention.', 'Shareable content.', 'Emotional connection.']} 
    },
    'services/conversion-rate-optimization.html': { 
        'hero_image': 'hero_marketing_creative_1770688454386.png', 
        'title': 'Conversion Rate Optimization', 
        'intro': "Traffic is vanity, conversion is sanity. We analyze user behavior and optimize your website to turn more visitors into paying customers.", 
        'services': [
            {
                'title': 'A/B Testing', 
                'desc': 'Comparing page variations.',
                'details': {
                    'long_desc': "Data-driven decisions. We run controlled experiments (A/B tests) where we show different versions of a page to users to see which one performs better.",
                    'quote': "Test everything.",
                    'bullet_title': 'Testing',
                    'bullets': ['Headline Tests', 'Button Colors', 'Layout Variations', 'Offer Testing'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }, 
            {
                'title': 'Heatmap Analysis', 
                'desc': 'Understanding user clicks and scrolls.',
                'details': {
                    'long_desc': "Visualizing behavior. We use heatmaps and scrollmaps to see exactly where users are clicking, how far they are scrolling, and where they are getting stuck.",
                    'quote': "See the clicks.",
                    'bullet_title': 'Heatmaps',
                    'bullets': ['Click Maps', 'Scroll Maps', 'Mouse Movement', 'Rage Clicks'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Funnel Optimization', 
                'desc': 'Removing friction from checkout.',
                'details': {
                    'long_desc': "Smooth the path. We analyze your signup or checkout funnel to identify drop-off points and remove friction, creating a smoother path to purchase.",
                    'quote': "Frictionless flow.",
                    'bullet_title': 'Funnels',
                    'bullets': ['Form Optimization', 'Checkout Flow', 'Trust Signals', 'Page Speed'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Copy Optimization', 
                'desc': 'Persuasive writing.',
                'details': {
                    'long_desc': "Persuasive words. We tweak the copy on your landing pages to better address user objections, highlight benefits, and create a stronger sense of urgency.",
                    'quote': "Words that convert.",
                    'bullet_title': 'Copywriting',
                    'bullets': ['Value Props', 'Microcopy', 'Social Proof', 'Urgency'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Maximize Value', 'items': ['Lower customer acquisition cost.', 'Increased revenue.', 'Better user insights.', 'Improved UX.']} 
    },
    
    'services/generative-ai.html': { 
        'hero_image': 'hero_emerging_tech_ai_1770688470055.png', 
        'title': 'Generative AI Solutions', 
        'intro': "Harness the creative power of AI. We build solutions using LLMs and generative models to automate content creation, personalization, and complex problem-solving.", 
        'services': [
            {
                'title': 'Custom LLM integration', 
                'desc': 'Fine-tuning GPT/Llama models.',
                'details': {
                    'long_desc': "Your own AI. We integrate and fine-tune Large Language Models (LLMs) like GPT-4 or Llama on your specific business data, ensuring relevant and accurate outputs.",
                    'quote': "Custom intelligence.",
                    'bullet_title': 'LLMs',
                    'bullets': ['API Integration', 'Fine-tuning', 'Prompt Engineering', 'RAG pipelines'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }, 
            {
                'title': 'AI Content Generators', 
                'desc': 'Automating text and image creation.',
                'details': {
                    'long_desc': "Create at scale. We build tools that use AI to automatically generate marketing copy, blog posts, product descriptions, or even custom images for your brand.",
                    'quote': "Automated creation.",
                    'bullet_title': 'Generators',
                    'bullets': ['Text Gen', 'Image Gen', 'Social Posts', 'Product Desc'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Smart Chatbots', 
                'desc': 'Context-aware customer support agents.',
                'details': {
                    'long_desc': "Chatbots that understand. Unlike old script-based bots, our GenAI chatbots can hold natural conversations, understand context, and answer complex queries based on your knowledge base.",
                    'quote': "Natural convo.",
                    'bullet_title': 'Chatbots',
                    'bullets': ['Support Agents', 'Internal Assistants', 'Context Aware', 'Multi-lingual'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Code Generation Tools', 
                'desc': 'Assisting development workflows.',
                'details': {
                    'long_desc': "Developer superpowers. We implement AI coding assistants and tools that can generate boilerplate code, write documentation, or create test cases automatically.",
                    'quote': "Faster coding.",
                    'bullet_title': 'DevTools',
                    'bullets': ['Copilot Integration', 'Doc Gen', 'Test Gen', 'Refactoring'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Creative Automation', 'items': ['Scale content production.', 'Personalize user experiences.', 'Automate complex reasoning.', 'Innovation leadership.']} 
    },
    'services/ar-vr-development.html': { 
        'hero_image': 'hero_emerging_tech_ai_1770688470055.png', 
        'title': 'AR/VR Development', 
        'intro': "Immersive realities are here. We build Augmented and Virtual Reality experiences for training, marketing, and entertainment that transport users to new worlds.", 
        'services': [
            {
                'title': 'AR Marketing Filters', 
                'desc': 'Instagram/Snapchat/WebAR effects.',
                'details': {
                    'long_desc': "Viral effects. We create interactive AR filters for social platforms that allow users to try on products virtually or engage with your brand in fun, shareable ways.",
                    'quote': "Try before buy.",
                    'bullet_title': 'AR Filters',
                    'bullets': ['Face Filters', 'World Effects', 'Virtual Try-on', 'WebAR'],
                    'image': 'hero_emerging_tech_ai_1770688470055.png'
                }
            }, 
            {
                'title': 'VR Training Simulations', 
                'desc': 'Safe environments for skill learning.',
                'details': {
                    'long_desc': "Risk-free training. We build VR simulations for industries like healthcare or manufacturing, allowing trainees to practice dangerous or expensive procedures in a safe virtual space.",
                    'quote': "Safe practice.",
                    'bullet_title': 'VR Training',
                    'bullets': ['Safety Drills', 'Medical Sim', 'Machine Ops', 'Soft Skills'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Virtual Showrooms', 
                'desc': '3D product exploration.',
                'details': {
                    'long_desc': "Walkthrough anywhere. We create immersive virtual showrooms where customers can explore your products or real estate properties from the comfort of their own home.",
                    'quote': "Virtual tour.",
                    'bullet_title': 'Showrooms',
                    'bullets': ['360 Tours', 'Product Config', 'Interactive Hotspots', 'VR Support'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Immersive Games', 
                'desc': 'Interactive VR entertainment.',
                'details': {
                    'long_desc': "Play in new worlds. We develop full-scale VR games and interactive experiences for headsets like Oculus/Meta Quest, pushing the boundaries of immersion.",
                    'quote': "Game on.",
                    'bullet_title': 'Gaming',
                    'bullets': ['Unity/Unreal', 'Oculus Quest', 'Full Immersion', 'Interactive Mechanics'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Immersion', 'items': ['Unforgettable experiences.', 'Deep user engagement.', 'Practical training tools.', 'Visualizing the impossible.']} 
    },
    'services/iot-solutions.html': { 
        'hero_image': 'hero_it_infrastructure_server_retry_1770688514971.png', 
        'title': 'Internet of Things (IoT)', 
        'intro': "Connect the physical and digital. We build end-to-end IoT solutions, from sensor data collection to cloud analytics and device control.", 
        'services': [
            {
                'title': 'Smart Home/Office', 
                'desc': 'Automation and energy management.',
                'details': {
                    'long_desc': "Intelligent spaces. We build systems that control lighting, HVAC, and security, automating environments for comfort and energy efficiency.",
                    'quote': "Smart spaces.",
                    'bullet_title': 'Automation',
                    'bullets': ['Lighting Control', 'Energy Mgmt', 'Smart Security', 'Voice Control'],
                    'image': 'hero_it_infrastructure_server_retry_1770688514971.png'
                }
            }, 
            {
                'title': 'Industrial IoT (IIoT)', 
                'desc': 'Predictive maintenance for machinery.',
                'details': {
                    'long_desc': "Industry 4.0. We connect industrial machinery to the cloud, monitoring vibration, temperature, and output to predict failures before they happen.",
                    'quote': "Predictive maintenance.",
                    'bullet_title': 'Industrial',
                    'bullets': ['Machine Monitoring', 'Predictive Maint', 'Digital Twin', 'OEE Tracking'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Asset Tracking', 
                'desc': 'Real-time location monitoring.',
                'details': {
                    'long_desc': "Track everything. Using GPS, BLE, or RFID, we build solutions to track high-value assets, vehicles, or inventory in real-time across your supply chain.",
                    'quote': "Real-time location.",
                    'bullet_title': 'Tracking',
                    'bullets': ['GPS/GSM', 'BLE Beacons', 'Geofencing', 'Supply Chain Visibility'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'IoT Dashboards', 
                'desc': 'Visualizing sensor data.',
                'details': {
                    'long_desc': "Data visibility. We build intuitive web and mobile dashboards that visualize the massive streams of data coming from your devices, making it actionable.",
                    'quote': "Visualize data.",
                    'bullet_title': 'Dashboards',
                    'bullets': ['Time-series Data', 'Alerting', 'Remote Control', 'Data Analytics'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }
        ], 
        'benefits': {'title': 'Connected Intelligence', 'items': ['Real-time operational visibility.', 'Predictive insights.', 'Automation of physical tasks.', 'New data streams.']} 
    },
    
    'services/wearable-app-development.html': { 
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png', 
        'title': 'Wearable App Development', 
        'intro': "Tech on your wrist. We design and develop apps for Apple Watch and WearOS, extending your digital presence to wearable devices.", 
        'services': [
            {
                'title': 'WatchOS Apps', 
                'desc': 'Native apps for Apple Watch.',
                'details': {
                    'long_desc': "Apple Watch experts. We build native apps for the Apple Watch using SwiftUI, leveraging the Digital Crown, haptics, and complications for a seamless wrist experience.",
                    'quote': "Apple native.",
                    'bullet_title': 'WatchOS',
                    'bullets': ['SwiftUI', 'Complications', 'HealthKit', 'Independent Apps'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }, 
            {
                'title': 'WearOS Development', 
                'desc': 'Apps for Android wearables.',
                'details': {
                    'long_desc': "Android wearables. We develop apps for the diverse ecosystem of WearOS devices (Samsung, Google Pixel Watch), ensuring compatibility and performance.",
                    'quote': "WearOS compatible.",
                    'bullet_title': 'WearOS',
                    'bullets': ['Modern Android', 'Tiles Support', 'Watch Face', 'Compatibility'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'Health Kit Integration', 
                'desc': 'Syncing fitness and health data.',
                'details': {
                    'long_desc': "Health data. We integrate deeply with HealthKit and Google Fit to read and write health data like heart rate, steps, and sleep, respecting user privacy.",
                    'quote': "Health sync.",
                    'bullet_title': 'Health',
                    'bullets': ['Heart Rate', 'Workouts', 'Sleep Tracking', 'Privacy First'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Companion Apps', 
                'desc': 'Extensions of phone apps.',
                'details': {
                    'long_desc': "Perfect companion. We design wearable apps that act as the perfect extension to your main mobile app, offering quick actions and notifications on the go.",
                    'quote': "On the go.",
                    'bullet_title': 'Companion',
                    'bullets': ['Notifications', 'Quick Actions', 'Data Sync', 'Remote Control'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ], 
        'benefits': {'title': 'Always On', 'items': ['Glanceable information.', 'Health & fitness tracking.', 'Instant notifications.', 'Hands-free convenience.']} 
    },
    'services/kotlin-app-development.html': { 
        'hero_image': 'hero_mobile_app_nodes_retry_1770688530429.png', 
        'title': 'Kotlin App Development', 
        'intro': "Modern Android excellence. We use Kotlin, Google's preferred language, to build safe, concise, and high-performance Android applications.", 
        'services': [
            {
                'title': 'Native Android Apps', 
                'desc': 'Pure Kotlin development.',
                'details': {
                    'long_desc': "Modern Android. We build 100% Kotlin apps that follow the latest Modern Android Development (MAD) standards, ensuring stability and maintainability.",
                    'quote': "Pure Kotlin.",
                    'bullet_title': 'Android Native',
                    'bullets': ['Coroutines', 'Flow', 'Dependency Injection', 'Material Design 3'],
                    'image': 'hero_mobile_app_nodes_retry_1770688530429.png'
                }
            }, 
            {
                'title': 'Kotlin Multiplatform', 
                'desc': 'Sharing logic across platforms.',
                'details': {
                    'long_desc': "Write once, run everywhere. We use Kotlin Multiplatform (KMP) to share business logic between Android and iOS execution, saving dev time while keeping native UI performance.",
                    'quote': "Shared logic.",
                    'bullet_title': 'KMP',
                    'bullets': ['Shared Business Logic', 'Native UI', 'iOS & Android', 'Code Reuse'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'App Migration', 
                'desc': 'Converting Java apps to Kotlin.',
                'details': {
                    'long_desc': "Modernize legacy. We help you migrate your legacy Java Android codebases to Kotlin, improving safety (null safety) and reducing boilerplate code.",
                    'quote': "Java to Kotlin.",
                    'bullet_title': 'Migration',
                    'bullets': ['Code Conversion', 'Refactoring', 'Testing', 'Null Safety'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Advanced UI', 
                'desc': 'Jetpack Compose interfaces.',
                'details': {
                    'long_desc': "Declarative UI. We build stunning interfaces using Jetpack Compose, Android's modern toolkit for building native UI, resulting in less code and more powerful layouts.",
                    'quote': "Jetpack Compose.",
                    'bullet_title': 'UI Toolkit',
                    'bullets': ['Declarative UI', 'Animation APIs', 'Theming', 'Interactive Preview'],
                    'image': 'hero_marketing_creative_1770688454386.png'
                }
            }
        ], 
        'benefits': {'title': 'Modern Standard', 'items': ['Fewer crashes (Null Safety).', 'Faster development.', 'Google supported.', 'Future-proof code.']} 
    },
    'services/golang-app-development.html': { 
        'hero_image': 'hero_software_dev_matrix_1770688395055.png', 
        'title': 'GoLang Development', 
        'intro': "Built for scale. We use Go (Golang) to build high-performance backends, microservices, and distributed systems that handle massive loads with ease.", 
        'services': [
            {
                'title': 'Microservices Architecture', 
                'desc': 'Decoupled, scalable services.',
                'details': {
                    'long_desc': "Decoupled power. We build robust microservices architectures using Go, allowing independent scaling and deployment of complex system components.",
                    'quote': "Scalable services.",
                    'bullet_title': 'Microservices',
                    'bullets': ['gRPC', 'Protobuf', 'Service Mesh', 'Independent Scaling'],
                    'image': 'hero_software_dev_matrix_1770688395055.png'
                }
            }, 
            {
                'title': 'High-Performance APIs', 
                'desc': 'Low latency REST/gRPC APIs.',
                'details': {
                    'long_desc': "Blazing fast. Go's efficiency makes it ideal for building high-throughput, low-latency APIs that power mobile apps and web frontends.",
                    'quote': "Low latency.",
                    'bullet_title': 'APIs',
                    'bullets': ['RESTful APIs', 'GraphQL', 'Middleware', 'Fast JSON processing'],
                    'image': 'hero_web_dev_futuristic_1770688377502.png'
                }
            }, 
            {
                'title': 'Cloud-Native Apps', 
                'desc': 'Optimized for Docker/Kubernetes.',
                'details': {
                    'long_desc': "Born for the cloud. Go compiles to a single binary, making it perfect for lightweight Docker containers and Kubernetes deployments.",
                    'quote': "Container ready.",
                    'bullet_title': 'Cloud Native',
                    'bullets': ['Small Binaries', 'Fast Startup', 'Docker Optimized', 'K8s Friendly'],
                    'image': 'hero_cloud_computing_ethereal_1770688425145.png'
                }
            }, 
            {
                'title': 'Concurrency Tools', 
                'desc': 'Processing massive data streams.',
                'details': {
                    'long_desc': "Parallel processing. We leverage Go's Goroutines and Channels to handle massive number of concurrent connections and data streams efficiently.",
                    'quote': "Concurrency.",
                    'bullet_title': 'Performance',
                    'bullets': ['Goroutines', 'Channels', 'Parallelism', 'Non-blocking I/O'],
                    'image': 'hero_data.png'
                }
            }
        ], 
        'benefits': {'title': 'Raw Performance', 'items': ['Extreme speed.', 'Efficient concurrency.', 'Low memory footprint.', 'Scalability at core.']} 
    },

}
