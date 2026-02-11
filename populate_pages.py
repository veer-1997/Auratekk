
import os
import re
import json
from content_data import content_data

# Global payload dictionary to store detailed content for the frontend
payload_data = {}

def slugify(text):
    """Converts a string into a slug suitable for IDs."""
    return re.sub(r'[^a-z0-9-]', '', text.lower().replace(' ', '-'))

# Read the template - we will use the index.html as base again to ensure
# we have the latest navigation updates
with open('index.html', 'r') as f:
    template_html = f.read()

def generate_populated_page(path, data):
    title = data['title']
    intro = data['intro']
    services = data['services']
    benefits = data.get('benefits', {}) # Benefits might be optional
    
    depth = path.count('/')
    prefix = '../' * depth if depth > 0 else './'
    
    content = template_html
    
    # 1. Update Resource Links (CSS, JS, Images) - Same logic as before
    content = re.sub(r'src="script.js"', f'src="{prefix}script.js"', content)
    content = re.sub(r'href="style.css"', f'href="{prefix}style.css"', content)
    content = re.sub(r'href="favicon.ico"', f'href="{prefix}favicon.ico"', content)
    content = re.sub(r'href="Artech_I.SVG"', f'href="{prefix}Artech_I.SVG"', content)
    content = re.sub(r'src="AURATEKK_DARK.svg"', f'src="{prefix}AURATEKK_DARK.svg"', content)
    content = re.sub(r'src="AURATEKK_LIGHT.svg"', f'src="{prefix}AURATEKK_LIGHT.svg"', content)
    content = re.sub(r'href="index.html"', f'href="{prefix}index.html"', content)
    content = re.sub(r'src="content_payload.js"', f'src="{prefix}content_payload.js"', content)
    
    # 2. Fix Navigation Links (Same logic as before)
    if depth > 0:
        for p_path in content_data.keys():
            link_in_index = p_path
            if link_in_index.startswith('services/'):
                new_link = link_in_index.replace('services/', '')
                content = content.replace(f'href="{link_in_index}"', f'href="{new_link}"')
            else:
                new_link = f'../{link_in_index}'
                content = content.replace(f'href="{link_in_index}"', f'href="{new_link}"')

    # Get Hero Image
    hero_image_filename = data.get('hero_image', 'luxury_hero.png') # Fallback if missing
    hero_image_path = f'{prefix}assets/images/heroes/{hero_image_filename}'


    # 3. Construct the HTML for the Service Cards
    services_html = ""
    for i, s in enumerate(services):
        # Staggered animation delay
        delay = 200 + (i * 100)
        
        # Generate ID and Store Details
        service_id = slugify(s['title'])
        if 'details' in s:
            payload_data[service_id] = s['details']
            payload_data[service_id]['title'] = s['title'] # Ensure title is available
        
        services_html += f'''
            <div onclick="openServiceModal('{service_id}')" class="group cursor-pointer p-8 rounded-3xl bg-slate-50 dark:bg-white/5 border border-slate-200 dark:border-white/10 hover:border-accent-gold/50 transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl hover:shadow-accent-gold/10 opacity-0 animate-[fadeInUp_0.8s_ease-out_{delay}ms_forwards]">
                <div class="mb-6 w-12 h-12 rounded-2xl bg-accent-gold/10 flex items-center justify-center group-hover:bg-accent-gold group-hover:text-black transition-colors duration-300">
                     <span class="material-symbols-outlined text-accent-gold group-hover:text-black transition-colors">arrow_forward</span>
                </div>
                <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-accent-gold transition-colors">{s['title']}</h3>
                <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">{s['desc']}</p>
            </div>
        '''

    # 4. Construct the HTML for Benefits
    benefits_html = ""
    if benefits:
        items_html = ""
        for item in benefits['items']:
            items_html += f'''
                <li class="flex items-start gap-3 opacity-0 animate-[fadeInUp_0.8s_ease-out_800ms_forwards]">
                    <span class="material-symbols-outlined text-accent-gold mt-1">check_circle</span>
                    <span class="text-slate-700 dark:text-slate-300">{item}</span>
                </li>
            '''
        
        benefits_html = f'''
            <div class="mt-20 p-8 md:p-12 rounded-3xl bg-accent-gold/5 border border-accent-gold/10 relative overflow-hidden group">
                 <div class="absolute inset-0 bg-gradient-to-br from-accent-gold/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
                <h2 class="font-display text-2xl md:text-3xl font-bold text-slate-900 dark:text-white mb-8 text-center relative z-10">{benefits['title']}</h2>
                <ul class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto relative z-10">
                    {items_html}
                </ul>
            </div>
        '''

    # 5. Build New Main Content
    new_main = f'''
        <main class="flex-1 pt-0">
            <!-- Hero Section -->
            <section class="relative h-[70vh] min-h-[650px] flex items-center justify-center overflow-hidden">
                <!-- Background Image & Overlay -->
                <div class="absolute inset-0 z-0 select-none">
                    <img src="{hero_image_path}" class="w-full h-full object-cover opacity-100 transition-transform duration-[20s] hover:scale-105 ease-linear transform-gpu animate-[kenburns_20s_infinite_alternate]" alt="{title} Background">
                    <div class="absolute inset-0 bg-background-dark/70 bg-blend-multiply"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/50 to-transparent"></div>
                </div>

                <div class="container mx-auto px-6 lg:px-10 relative z-10 text-center mt-20">
                    <div class="flex flex-col items-center gap-6 max-w-4xl mx-auto">
                        <div class="inline-flex items-center gap-2 text-sm text-accent-gold/80 bg-black/30 backdrop-blur-md px-4 py-1.5 rounded-full border border-white/10 opacity-0 animate-[fadeInUp_0.8s_ease-out_forwards]">
                            <a href="{prefix}index.html" class="hover:text-white transition-colors">Home</a>
                            <span class="material-symbols-outlined text-[10px]">chevron_right</span>
                            <span class="text-white">{title}</span>
                        </div>
                        <h1 class="font-display text-5xl md:text-7xl lg:text-8xl font-bold text-white leading-tight opacity-0 animate-[fadeInUp_0.8s_ease-out_200ms_forwards] drop-shadow-2xl">
                            {title}
                        </h1>
                        <p class="text-slate-200 text-lg md:text-xl leading-relaxed max-w-2xl opacity-0 animate-[fadeInUp_0.8s_ease-out_400ms_forwards] drop-shadow-md">
                            {intro}
                        </p>
                        <div class="pt-8 opacity-0 animate-[fadeInUp_0.8s_ease-out_600ms_forwards]">
                            <a href="javascript:void(0)" onclick="openContactModal()" class="group relative inline-flex items-center justify-center px-8 py-4 bg-accent-gold text-black font-bold uppercase tracking-widest rounded-full hover:shadow-[0_0_20px_rgba(197,160,89,0.5)] active:scale-95 transition-all duration-300 overflow-hidden">
                                <span class="relative z-10 group-hover:text-white transition-colors">Start a Project</span>
                                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300"></div>
                            </a>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Content Section -->
            <section class="py-20 md:py-32 bg-white dark:bg-background-dark relative overflow-hidden">
                 <!-- Decorative Elements -->
                 <div class="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-accent-gold/30 to-transparent"></div>
                 
                <div class="container mx-auto px-6 lg:px-10 relative z-10">
                   <!-- Services Grid -->
                   <div class="grid md:grid-cols-2 lg:grid-cols-2 gap-8 mb-12">
                        {services_html}
                   </div>
                   
                   <!-- Benefits Section -->
                   {benefits_html}
                   
                   <!-- CTA Section -->
                   <div class="mt-32 text-center opacity-0 animate-[fadeInUp_1s_ease-out_1000ms_forwards]">
                        <p class="font-mono text-sm text-accent-gold uppercase tracking-widest mb-4">Ready to elevate your business?</p>
                        <h2 class="font-display text-3xl md:text-5xl font-bold text-slate-900 dark:text-white mb-8">Let's build something <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-accent-gold to-yellow-200">extraordinary</span> together.</h2>
                        <a href="javascript:void(0)" onclick="openContactModal()" class="inline-flex items-center justify-center px-10 py-5 border border-slate-200 dark:border-white/20 text-slate-900 dark:text-white font-bold uppercase tracking-widest rounded-full hover:bg-white/5 hover:border-accent-gold transition-all duration-300">
                            Contact Our Experts
                        </a>
                   </div>
                </div>
            </section>
        </main>
    '''
    
    # Replace <main> block
    content = re.sub(r'<main class="flex-1">.*?</main>', new_main, content, flags=re.DOTALL)
    
    # Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{title} | Auratekk (Aura Tech)</title>', content)
    
    # Write File
    with open(path, 'w') as f:
        f.write(content)
    print(f"Populated {path}")

# Run population for all pages
for path, data in content_data.items():
    if not os.path.exists('services') and '/' in path:
         os.makedirs('services', exist_ok=True)
         
    generate_populated_page(path, data)

# Generate content_payload.js
with open('content_payload.js', 'w') as f:
    js_content = f"const serviceDetails = {json.dumps(payload_data, indent=4)};"
    f.write(js_content)
    print("Generated content_payload.js with detailed service data.")
