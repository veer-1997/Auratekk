import os
import re

# Read the template
with open('index.html', 'r') as f:
    template_html = f.read()

# Pages configuration
pages = [
    # Top Level
    {'path': 'technologies.html', 'title': 'Technologies'},
    {'path': 'industries.html', 'title': 'Industries'},
    {'path': 'about-us.html', 'title': 'About Us'},
    {'path': 'careers.html', 'title': 'Careers'},
    
    # Web Development
    {'path': 'services/web-development.html', 'title': 'Web Development'},
    {'path': 'services/wordpress-development.html', 'title': 'WordPress Development'},
    {'path': 'services/ecommerce-development.html', 'title': 'E-Commerce Web Development'},
    {'path': 'services/custom-cms-development.html', 'title': 'Custom CMS Development'},
    
    # Software Development
    {'path': 'services/custom-software-development.html', 'title': 'Custom Software Development'},
    {'path': 'services/mvp-development.html', 'title': 'MVP Development'},
    {'path': 'services/devops-services.html', 'title': 'DevOps Services'},
    
    # Mobile App
    {'path': 'services/ios-app-development.html', 'title': 'iOS App Development'},
    {'path': 'services/android-app-development.html', 'title': 'Android App Development'},
    {'path': 'services/react-native-development.html', 'title': 'React Native Development'},
    {'path': 'services/flutter-app-development.html', 'title': 'Flutter App Development'},
    
    # Other Services
    {'path': 'services/branding-design.html', 'title': 'Branding & Design'},
    {'path': 'services/digital-marketing.html', 'title': 'Digital Marketing (SEO/PPC)'},
    {'path': 'services/emerging-tech.html', 'title': 'Emerging Tech (AI/AR/VR)'},
    {'path': 'services/cloud-consulting.html', 'title': 'Cloud Consulting (AWS/Azure)'},
    
    # Infrastructure
    {'path': 'services/it-infrastructure-setup.html', 'title': 'IT Infrastructure Setup'},
    {'path': 'services/on-prem-cloud-setup.html', 'title': 'On-Prem & Cloud Setup'},
    {'path': 'services/server-network-mgmt.html', 'title': 'Server & Network Mgmt'},
    
    # Cloud & Hosting
    {'path': 'services/hosting-management.html', 'title': 'Hosting Management'},
    {'path': 'services/cloud-migration.html', 'title': 'Cloud Migration'},
    {'path': 'services/backup-disaster-recovery.html', 'title': 'Backup & Disaster Recovery'},
    
    # Managed IT
    {'path': 'services/it-support-maintenance.html', 'title': 'IT Support & Maintenance'},
    {'path': 'services/remote-monitoring.html', 'title': 'Remote Monitoring'},
    {'path': 'services/patch-management.html', 'title': 'Patch Management'},
    
    # Cybersecurity
    {'path': 'services/security-assessments.html', 'title': 'Security Assessments'},
    {'path': 'services/firewall-endpoint-protection.html', 'title': 'Firewall & Endpoint Protection'},
    {'path': 'services/identity-access-mgmt.html', 'title': 'Identity Access Mgmt'},
]

# Ensure services directory exists
if not os.path.exists('services'):
    os.makedirs('services')

def generate_page(page_config):
    path = page_config['path']
    title = page_config['title']
    
    depth = path.count('/')
    prefix = '../' * depth if depth > 0 else './'
    
    content = template_html
    
    # 1. Update Resource Links (CSS, JS, Images)
    # Fix Script src="script.js" -> src="{prefix}script.js"
    content = re.sub(r'src="script.js"', f'src="{prefix}script.js"', content)
    content = re.sub(r'href="style.css"', f'href="{prefix}style.css"', content)
    content = re.sub(r'href="favicon.ico"', f'href="{prefix}favicon.ico"', content)
    content = re.sub(r'href="Artech_I.SVG"', f'href="{prefix}Artech_I.SVG"', content)
    
    # Fix Image src="AURATEKK_DARK.svg" -> src="{prefix}AURATEKK_DARK.svg"
    content = re.sub(r'src="AURATEKK_DARK.svg"', f'src="{prefix}AURATEKK_DARK.svg"', content)
    content = re.sub(r'src="AURATEKK_LIGHT.svg"', f'src="{prefix}AURATEKK_LIGHT.svg"', content)
    
    # Fix Navigation Links to Home
    content = re.sub(r'href="index.html"', f'href="{prefix}index.html"', content)
    
    # 2. Fix Navigation Links to Other Pages
    # We need to iterate through all defined pages and fix their links in the content
    # assuming index.html has links like "services/web-development.html" or "about-us.html"
    if depth > 0:
        for p in pages:
            link_in_index = p['path']
            if link_in_index.startswith('services/'):
                # Link is to a service page
                # If we are in services/, we remove 'services/' prefix
                new_link = link_in_index.replace('services/', '')
                content = content.replace(f'href="{link_in_index}"', f'href="{new_link}"')
            else:
                # Link is to a root page (e.g. about-us.html)
                # If we are in services/, we add '../' prefix
                new_link = f'../{link_in_index}'
                content = content.replace(f'href="{link_in_index}"', f'href="{new_link}"')
    
    # 3. Add New Main Content
    new_main = f'''
        <main class="flex-1 pt-20">
            <section class="relative py-24 bg-background-light dark:bg-background-dark overflow-hidden">
                <div class="absolute inset-0 bg-accent-gold/5 pointer-events-none"></div>
                <!-- Background decorative elements -->
                <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-accent-gold/5 to-transparent pointer-events-none"></div>

                <div class="container mx-auto px-6 lg:px-10 relative z-10">
                    <div class="flex flex-col gap-4">
                        <div class="inline-flex items-center gap-2 text-sm text-slate-500 dark:text-slate-400">
                            <a href="{prefix}index.html" class="hover:text-accent-gold transition-colors">Home</a>
                            <span class="material-symbols-outlined text-xs">chevron_right</span>
                            <span class="text-accent-gold">{title}</span>
                        </div>
                        <h1 class="font-display text-4xl md:text-6xl font-bold text-slate-900 dark:text-white leading-tight">
                            {title}
                        </h1>
                        <p class="text-slate-600 dark:text-slate-300 text-lg md:text-xl max-w-2xl mt-4">
                            Premium {title} solutions designed to elevate your business performance and digital presence.
                        </p>
                    </div>
                </div>
            </section>
            
            <section class="py-20 bg-white dark:bg-black/20">
                <div class="container mx-auto px-6 lg:px-10">
                   <div class="prose dark:prose-invert max-w-4xl mx-auto">
                        <div class="flex flex-col items-center justify-center p-12 border border-dashed border-slate-300 dark:border-slate-700 rounded-2xl bg-slate-50 dark:bg-slate-900/50">
                            <span class="material-symbols-outlined text-6xl text-accent-gold mb-4">construction</span>
                            <h2 class="text-2xl font-bold text-slate-800 dark:text-white mb-2">Content Coming Soon</h2>
                            <p class="text-slate-600 dark:text-slate-400 text-center">
                                We are currently crafting detailed information for our <strong>{title}</strong> service. 
                                <br>Please check back shortly or <a href="#contact" class="text-accent-gold hover:underline">contact us</a> for immediate assistance.
                            </p>
                        </div>
                   </div>
                </div>
            </section>
        </main>
    '''
    
    # Replace the existing <main>...</main> block
    # Using regex with DOTALL to match across newlines
    content = re.sub(r'<main class="flex-1">.*?</main>', new_main, content, flags=re.DOTALL)
    
    # 4. Update Title Tag
    content = re.sub(r'<title>.*?</title>', f'<title>{title} - Aura Tech</title>', content)
    
    # 5. Write to file
    with open(path, 'w') as f:
        f.write(content)
    print(f"Generated {path}")

# Run generation
for page in pages:
    generate_page(page)
