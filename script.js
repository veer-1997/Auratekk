
// Tailwind Config
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#13a4ec",
                "background-light": "#f6f7f8",
                "background-dark": "#05090B",
                "background-panel": "#0B1013",
                "background-panel-light": "#f0f2f4",
                "accent-gold": "#C5A059",
                "accent-sand": "#E6DCCA",
                "neon-gold": "#FCD34D",
                "brand-teal": "#14b8a6",
                "brand-red": "#dc2626",
                "card-coral": "#FF8F8F",
                "card-cyan": "#4DFCC6",
                "card-gray": "#E2E8F0",
            },
            fontFamily: {
                "display": ["Space Grotesk", "sans-serif"],
                "body": ["Inter", "sans-serif"],
                "mono": ["Space Mono", "monospace"],
            },
            backgroundImage: {
                'cyber-grid': 'linear-gradient(rgba(197, 160, 89, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(197, 160, 89, 0.05) 1px, transparent 1px)',
                'glass-gradient': 'linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.005) 100%)',
                'glass-gradient-light': 'linear-gradient(145deg, rgba(255,255,255,0.7) 0%, rgba(255,255,255,0.3) 100%)',
                'gold-glow': 'radial-gradient(circle at center, rgba(197, 160, 89, 0.2) 0%, transparent 70%)',
                'portal-glow': 'radial-gradient(circle at center, rgba(19, 164, 236, 0.15) 0%, transparent 60%)',
                'robot-glow': 'radial-gradient(circle at center, rgba(197, 160, 89, 0.15) 0%, transparent 50%)',
            },
            boxShadow: {
                'neon': '0 0 15px rgba(197, 160, 89, 0.3), 0 0 30px rgba(197, 160, 89, 0.1)',
                'neon-blue': '0 0 15px rgba(19, 164, 236, 0.3), 0 0 30px rgba(19, 164, 236, 0.1)',
                'neon-red': '0 0 15px rgba(220, 38, 38, 0.3), 0 0 30px rgba(220, 38, 38, 0.1)',
                'glass-lg': '0 25px 50px -12px rgba(0, 0, 0, 0.5)',
                'card-float': '0 20px 40px -5px rgba(0,0,0,0.4), 0 10px 20px -5px rgba(0,0,0,0.3)',
                'soft-shadow': '0 8px 30px rgba(0,0,0,0.04)',
            },
            animation: {
                'float': 'float 6s ease-in-out infinite',
                'float-slow': 'float 8s ease-in-out infinite',
                'float-delayed': 'float 7s ease-in-out 1s infinite',
                'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'spin-slow': 'spin 60s linear infinite',
                'scan': 'scan 4s linear infinite',
                'orb-spin': 'orbSpin 20s linear infinite',
            },
            keyframes: {
                float: {
                    '0%, 100%': { transform: 'translateY(0)' },
                    '50%': { transform: 'translateY(-15px)' },
                },
                scan: {
                    '0%': { transform: 'translateY(-100%)' },
                    '100%': { transform: 'translateY(100%)' },
                },
                orbSpin: {
                    '0%': { transform: 'rotate(0deg)' },
                    '100%': { transform: 'rotate(360deg)' },
                }
            }
        },
    },
};

// Theme Management Logic
document.addEventListener('DOMContentLoaded', () => {
    const html = document.documentElement;
    const themeToggleBtns = document.querySelectorAll('#theme-toggle');

    // Check local storage or system preference
    if (localStorage.theme === 'dark' || (!('theme' in localStorage))) {
        html.classList.add('dark');
        updateIcons(true);
    } else {
        html.classList.remove('dark');
        updateIcons(false);
    }



    // --- Header Scroll Logic ---
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // --- 3D Hero Scene Implementation ---
    const heroScene = initHeroScene();

    // Initial Theme Update for 3D Scene
    if (heroScene) {
        heroScene.updateTheme(html.classList.contains('dark'));
    }

    // --- Loading Screen Logic ---
    const loader = document.getElementById('loader-overlay');
    if (loader) {
        // Check if intro has been shown in this session
        if (sessionStorage.getItem('auratekk_intro_shown')) {
            // Immediately remove loader if already shown
            loader.style.display = 'none'; // Ensure it's hidden immediately
            loader.remove();
            document.body.classList.remove('overflow-hidden');
        } else {
            // First time visit in this session: Play animation
            // Wait for animations to finish (approx 2.5s + buffer)
            setTimeout(() => {
                loader.classList.add('animate-slide-up');

                // Remove from DOM after slide-up animation
                setTimeout(() => {
                    loader.remove();
                    document.body.classList.remove('overflow-hidden');
                    // Mark as shown for this session
                    sessionStorage.setItem('auratekk_intro_shown', 'true');
                }, 800);
            }, 2800);
        }
    }

    // Toggle Functionality
    themeToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            html.classList.toggle('dark');
            const isDark = html.classList.contains('dark');

            // Save preference
            localStorage.theme = isDark ? 'dark' : 'light';

            updateIcons(isDark);

            // Update 3D Scene Colors
            if (heroScene) {
                heroScene.updateTheme(isDark);
            }
        });
    });

    function updateIcons(isDark) {
        themeToggleBtns.forEach(btn => {
            const icon = btn.querySelector('.material-symbols-outlined');
            if (icon) {
                icon.textContent = isDark ? 'light_mode' : 'dark_mode';
            }
        });
    }

    // --- Mobile Menu Logic ---
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileAccordionTriggers = document.querySelectorAll('.mobile-accordion-trigger');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('translate-x-full');
            document.body.classList.add('overflow-hidden');
        });
    }

    if (mobileMenuClose && mobileMenu) {
        mobileMenuClose.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
            document.body.classList.remove('overflow-hidden');
        });
    }

    // Mobile Accordion Logic
    mobileAccordionTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const content = trigger.nextElementSibling;
            const icon = trigger.querySelector('.material-symbols-outlined');

            // Toggle Hidden Class
            content.classList.toggle('hidden');

            // Rotate Icon
            if (content.classList.contains('hidden')) {
                icon.style.transform = 'rotate(0deg)';
            } else {
                icon.style.transform = 'rotate(180deg)';
            }
        });
    });

    // Demo Carousel Navigation
    const demoCarousel = document.getElementById('demo-carousel');
    const scrollLeftBtn = document.getElementById('demo-scroll-left');
    const scrollRightBtn = document.getElementById('demo-scroll-right');

    if (demoCarousel && scrollLeftBtn && scrollRightBtn) {
        scrollLeftBtn.addEventListener('click', () => {
            demoCarousel.scrollBy({
                left: -400,
                behavior: 'smooth'
            });
        });

        scrollRightBtn.addEventListener('click', () => {
            demoCarousel.scrollBy({
                left: 400,
                behavior: 'smooth'
            });
        });
    }

    // Custom Cursor Animation
    function initCustomCursor() {
        // Only on desktop devices
        if (window.innerWidth <= 768) return;

        // Create cursor elements
        const cursor = document.createElement('div');
        cursor.classList.add('custom-cursor');
        const cursorDot = document.createElement('div');
        cursorDot.classList.add('custom-cursor-dot');

        document.body.appendChild(cursor);
        document.body.appendChild(cursorDot);

        let mouseX = 0, mouseY = 0;
        let cursorX = 0, cursorY = 0;
        let dotX = 0, dotY = 0;

        // Track mouse position
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });

        // Smooth animation loop
        function animate() {
            // Smooth follow for outer ring
            cursorX += (mouseX - cursorX) * 0.15;
            cursorY += (mouseY - cursorY) * 0.15;

            // Faster follow for inner dot
            dotX += (mouseX - dotX) * 0.25;
            dotY += (mouseY - dotY) * 0.25;

            cursor.style.left = cursorX + 'px';
            cursor.style.top = cursorY + 'px';
            cursorDot.style.left = dotX + 'px';
            cursorDot.style.top = dotY + 'px';

            requestAnimationFrame(animate);
        }
        animate();

        // Add hover effects for interactive elements
        const interactiveElements = document.querySelectorAll('a, button, .cursor-pointer, [onclick]');
        interactiveElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.classList.add('hover');
                cursorDot.classList.add('hover');
            });
            el.addEventListener('mouseleave', () => {
                cursor.classList.remove('hover');
                cursorDot.classList.remove('hover');
            });
        });

        // Hide cursor when leaving window
        document.addEventListener('mouseleave', () => {
            cursor.style.opacity = '0';
            cursorDot.style.opacity = '0';
        });
        document.addEventListener('mouseenter', () => {
            cursor.style.opacity = '1';
            cursorDot.style.opacity = '0.8';
        });
    }

    initCustomCursor();
});

function initHeroScene() {
    const container = document.getElementById('hero-canvas-container');
    if (!container) return;

    // Scene Setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // --- Create a Root Group to shift everything to the RIGHT ---
    const sceneRoot = new THREE.Group();
    sceneRoot.position.x = 5; // Positive X moves objects to the right
    scene.add(sceneRoot);

    // Particle Network
    const particlesGeometry = new THREE.BufferGeometry();
    const particlesCount = 700;

    const posArray = new Float32Array(particlesCount * 3);

    for (let i = 0; i < particlesCount * 3; i++) {
        // Spread particles in a large sphere/cloud
        posArray[i] = (Math.random() - 0.5) * 15; // Spread range
    }

    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

    // Material
    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.03,
        color: 0xC5A059, // Accent Gold
        transparent: true,
        opacity: 0.8,
    });

    // Create Mesh
    const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
    sceneRoot.add(particlesMesh);

    // Connecting Lines (Optional for "Network" feel - basic implementation)
    // For performance, we might simulate connection via visual density or use a LineSegments
    // Let's create a secondary geometric shape (Icosahedron wireframe) to represent "Structure"
    const geoGeometry = new THREE.IcosahedronGeometry(4, 1);
    const geoMaterial = new THREE.MeshBasicMaterial({
        color: 0x13a4ec, // Primary Blue
        wireframe: true,
        transparent: true,
        opacity: 0.15
    });
    const geoMesh = new THREE.Mesh(geoGeometry, geoMaterial);
    sceneRoot.add(geoMesh);

    // --- Diverse Elements ---
    const shapesGroup = new THREE.Group();
    sceneRoot.add(shapesGroup);

    const geometries = [
        new THREE.TorusGeometry(0.6, 0.05, 16, 100), // Ring 1
        new THREE.TorusGeometry(0.4, 0.02, 16, 100), // Ring 2 (thinner)
        new THREE.TorusGeometry(0.8, 0.03, 16, 100)  // Ring 3 (larger)
    ];

    const materials = [
        new THREE.MeshBasicMaterial({ color: 0x13a4ec, wireframe: true, transparent: true, opacity: 0.3 }),
        new THREE.MeshBasicMaterial({ color: 0xC5A059, wireframe: true, transparent: true, opacity: 0.3 }),
        new THREE.MeshBasicMaterial({ color: 0xFFFFFF, wireframe: true, transparent: true, opacity: 0.1 })
    ];

    for (let i = 0; i < 15; i++) {
        const geometry = geometries[Math.floor(Math.random() * geometries.length)];
        const material = materials[Math.floor(Math.random() * materials.length)];
        const mesh = new THREE.Mesh(geometry, material);

        // Random position spread
        mesh.position.x = (Math.random() - 0.5) * 30;
        mesh.position.y = (Math.random() - 0.5) * 20;
        mesh.position.z = (Math.random() - 0.5) * 15;

        // Random rotation
        mesh.rotation.x = Math.random() * Math.PI;
        mesh.rotation.y = Math.random() * Math.PI;

        // Add custom float data
        mesh.userData = {
            floatSpeed: 0.005 + Math.random() * 0.01,
            rotationSpeed: 0.005 + Math.random() * 0.01
        };

        shapesGroup.add(mesh);
    }

    // --- SVG Background Elements ---
    const textureLoader = new THREE.TextureLoader();

    // Helper to create floating SVG plane
    const createSVGPlane = (path, size, x, y, z, floatSpeed, rotSpeed) => {
        textureLoader.load(path, (texture) => {
            const geometry = new THREE.PlaneGeometry(size, size);
            const material = new THREE.MeshBasicMaterial({
                map: texture,
                transparent: true,
                opacity: 1.0, // Full opacity
                side: THREE.DoubleSide,
                depthWrite: false // Don't block other objects behind
            });
            const mesh = new THREE.Mesh(geometry, material);

            // Adjust Z to be visible
            mesh.position.set(x, y, z);
            mesh.userData = {
                originalY: y,
                floatSpeed: floatSpeed,
                rotSpeed: rotSpeed,
                randomOffset: Math.random() * 100
            };

            sceneRoot.add(mesh); // Add to shifted root
            svgMeshes.push(mesh);
        });
    };

    const svgMeshes = [];

    // Add ore_dark.SVG (Background Element 1)
    createSVGPlane('ore_dark.SVG', 8, 2, 4, -4, 0.4, 0.001);

    // Add Artech_I.SVG (Background Element 2)
    createSVGPlane('Artech_I.SVG', 7, 5, -5, -6, 0.6, -0.002);

    // Camera Position
    camera.position.z = 10;
    camera.position.y = 0;

    // Mouse Interaction
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;

    const windowHalfX = window.innerWidth / 2;
    const windowHalfY = window.innerHeight / 2;

    document.addEventListener('mousemove', (event) => {
        mouseX = (event.clientX - windowHalfX);
        mouseY = (event.clientY - windowHalfY);
    });

    // Animation Loop
    const clock = new THREE.Clock();

    const animate = () => {
        requestAnimationFrame(animate);
        const elapsedTime = clock.getElapsedTime();

        targetX = mouseX * 0.0005;
        targetY = mouseY * 0.0005;

        // Smooth rotation based on mouse - Rotate the ROOT group for parallax
        sceneRoot.rotation.y += 0.02 * (targetX - sceneRoot.rotation.y);
        sceneRoot.rotation.x += 0.02 * (targetY - sceneRoot.rotation.x);

        // Individual element rotations
        particlesMesh.rotation.y += 0.001;
        geoMesh.rotation.x -= 0.001;
        geoMesh.rotation.y -= 0.001;

        // Animate shapes
        shapesGroup.children.forEach(mesh => {
            mesh.rotation.x += mesh.userData.rotationSpeed;
            mesh.rotation.y += mesh.userData.rotationSpeed;
            mesh.position.y += Math.sin(elapsedTime * mesh.userData.floatSpeed) * 0.02;
        });

        // Animate SVG planes
        svgMeshes.forEach(mesh => {
            // Gentle float
            mesh.position.y = mesh.userData.originalY + Math.sin(elapsedTime * mesh.userData.floatSpeed + mesh.userData.randomOffset) * 0.5;
            // Gentle rotation
            mesh.rotation.z += mesh.userData.rotSpeed;
        });

        // Pulse effect for geometry
        const scale = 1 + Math.sin(elapsedTime * 0.5) * 0.05;
        geoMesh.scale.set(scale, scale, scale);

        renderer.render(scene, camera);
    };

    animate();

    // Handle window resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // --- Theme Update Logic ---
    function updateTheme(isDark) {
        if (isDark) {
            // Dark Mode Colors
            particlesMaterial.color.setHex(0xC5A059); // Gold
            particlesMaterial.opacity = 0.8;

            geoMaterial.color.setHex(0x13a4ec); // Blue
            geoMaterial.opacity = 0.15;

            materials[0].color.setHex(0x13a4ec); // Blue
            materials[1].color.setHex(0xC5A059); // Gold
            materials[2].color.setHex(0xFFFFFF); // White
            materials[2].opacity = 0.1;

            scene.fog = null; // No fog or clear fog
        } else {
            // Light Mode Colors - High Contrast
            particlesMaterial.color.setHex(0xB08D55); // Darker Gold
            particlesMaterial.opacity = 0.9;

            geoMaterial.color.setHex(0x0F8BC7); // Darker Blue
            geoMaterial.opacity = 0.3; // More visible

            materials[0].color.setHex(0x0F8BC7); // Darker Blue
            materials[1].color.setHex(0xB08D55); // Darker Gold
            materials[2].color.setHex(0x1a1a1a); // Almost Black (replacing White)
            materials[2].opacity = 0.2; // Increase opacity
        }
    }

    return { updateTheme };
}

// --- Generic Modal Functions ---
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    modal.classList.remove('hidden');
    modal.classList.add('flex');

    // Trigger animation
    setTimeout(() => {
        modal.style.opacity = '0';
        modal.style.transform = 'scale(0.95)';
        modal.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out';

        requestAnimationFrame(() => {
            modal.style.opacity = '1';
            modal.style.transform = 'scale(1)';
        });
    }, 10);

    // Prevent body scroll
    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    // Animate out
    modal.style.opacity = '0';
    modal.style.transform = 'scale(0.95)';

    setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');

        // Only reset overflow if no other modals are open (simple check)
        // For now, we assume only one modal is open at a time for simplicity
        document.body.style.overflow = '';
    }, 300);
}

// --- Industry Modal Functions ---
function openIndustryModal(industryId) {
    const allContent = document.querySelectorAll('.industry-content');
    const targetContent = document.getElementById(`modal-${industryId}`);

    // Hide all industry content
    allContent.forEach(content => content.classList.add('hidden'));

    // Show target industry content
    if (targetContent) {
        targetContent.classList.remove('hidden');
    }

    openModal('industryModal');
}

function closeIndustryModal() {
    closeModal('industryModal');
}

// Close modal on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeIndustryModal();
        closeServiceModal();
        closeContactModal();
    }
});

// --- Service Modal Functions (Dynamic) ---
function openServiceModal(serviceId) {
    if (typeof serviceDetails === 'undefined') {
        console.error("Service details payload not loaded");
        return;
    }

    const modal = document.getElementById('service-modal');
    const details = serviceDetails[serviceId];

    if (!modal) {
        console.error("Service modal element not found");
        return;
    }

    if (!details) {
        console.error("Details not found for service ID:", serviceId);
        // Fallback or just return?
        return;
    }

    // Populate Content
    const title = details.title || 'Service Details';
    const titleEl = document.getElementById('modal-title');
    const titleMobileEl = document.getElementById('modal-title-mobile');
    if (titleEl) titleEl.textContent = title;
    if (titleMobileEl) titleMobileEl.textContent = title;

    const descEl = document.getElementById('modal-description');
    if (descEl) descEl.textContent = details.long_desc || '';

    const quoteEl = document.getElementById('modal-quote');
    if (quoteEl) quoteEl.textContent = details.quote || '';

    // Image Handling
    const imgEl = document.getElementById('modal-image');
    if (imgEl && details.image) {
        let prefix = '';
        // Simple check for subdirectory
        if (window.location.pathname.includes('/services/') || window.location.href.includes('/services/')) {
            prefix = '../';
        }
        imgEl.src = `${prefix}assets/images/heroes/${details.image}`;
    }

    // Bullets
    const bulletList = document.getElementById('modal-bullets');
    if (bulletList) {
        bulletList.innerHTML = ''; // Clear existing
        if (details.bullets && Array.isArray(details.bullets)) {
            details.bullets.forEach(bullet => {
                const li = document.createElement('li');
                li.className = "flex items-start gap-3";
                li.innerHTML = `
                    <span class="material-symbols-outlined text-accent-gold mt-1 text-sm">arrow_right_alt</span>
                    <span class="text-slate-600 dark:text-slate-300 text-base">${bullet}</span>
                `;
                bulletList.appendChild(li);
            });
        }
    }

    // Show Modal
    modal.classList.remove('hidden');
    modal.classList.add('flex');

    // Animation
    setTimeout(() => {
        const backdrop = document.getElementById('modal-backdrop');
        const content = document.getElementById('modal-content');

        if (backdrop) backdrop.classList.remove('opacity-0');
        if (content) {
            content.classList.remove('opacity-0', 'scale-95');
            content.classList.add('scale-100');
        }
    }, 10);

    document.body.style.overflow = 'hidden';
}

function closeServiceModal() {
    const modal = document.getElementById('service-modal');
    if (!modal) return;

    const backdrop = document.getElementById('modal-backdrop');
    const content = document.getElementById('modal-content');

    if (backdrop) backdrop.classList.add('opacity-0');
    if (content) {
        content.classList.remove('scale-100');
        content.classList.add('opacity-0', 'scale-95');
    }

    setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }, 300);
}

// --- Contact Modal Logic ---
function openContactModal() {
    openModal('contactModal');
}

function closeContactModal() {
    closeModal('contactModal');
}

// --- Path to Success Animation ---
document.addEventListener('DOMContentLoaded', () => {
    const section = document.getElementById('path-to-success-section');
    const orb = document.getElementById('catalyst-orb');
    const stages = document.querySelectorAll('.success-stage');

    if (!section || !orb || stages.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                runSuccessAnimation();
                observer.unobserve(section); // Run once or keep observing for replay? let's run once for now.
            }
        });
    }, { threshold: 0.5 });

    observer.observe(section);

    function runSuccessAnimation() {
        // Animate Orb
        // We want the orb to travel from left to right across the container width
        // The container is relative.
        // Let's use simple CSS transition or explicit Keyframes logic via JS for sync

        // Reset
        stages.forEach(stage => stage.classList.remove('active-stage'));
        orb.style.transition = 'none';
        orb.style.left = '0%';
        orb.style.opacity = '1';

        // Start Orb Travel
        setTimeout(() => {
            orb.style.transition = 'left 2s linear'; // 2 seconds to cross
            orb.style.left = '100%';
        }, 100);

        // Trigger words based on timing
        // Total time 2000ms. 6 words.
        // impact times roughly: 10%, 25%, 45%, 65%, 80%, 95%
        // Let's just stagger them evenly for visual flow
        const triggers = [200, 500, 800, 1100, 1400, 1700];

        triggers.forEach((time, index) => {
            if (stages[index]) {
                setTimeout(() => {
                    stages[index].classList.add('active-stage');
                    // Optional: hit effect on orb?
                }, time);
            }
        });

        // Hide orb after it passes? Or let it zip off.
        setTimeout(() => {
            orb.style.opacity = '0';
        }, 2200);
    }
});

// --- Supabase Integration ---
// CONFIGURATION: Update Supabase credentials here
const SUPABASE_URL = "https://khqoziafbfgfaxvnwiyy.supabase.co";
const SUPABASE_ANON_KEY = "sb_publishable_V6BPhOMhOj2-kIM58jqcqQ_TPLNgPmU";

// Initialize Supabase Client
// Ensure the Supabase JS library is loaded in your HTML (<script src=".../supabase-js"></script>)
let supabaseClient = null;
if (typeof supabase !== 'undefined') {
    try {
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } catch (e) {
        console.error('Supabase Initialization Error:', e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Select the form by ID
    const form = document.getElementById("contactForm");

    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault(); // Prevent default page reload

            // Collect form values
            // Only send fields that exist in Supabase table: full_name, phone_number, company_name
            const payload = {
                full_name: document.getElementById('full_name').value.trim(),
                phone_number: document.getElementById('phone_number').value.trim(),
                company_name: document.getElementById('company_name').value.trim()
            };

            // Insert into Supabase 'inquiries' table
            // Ensure your table columns match these keys exactly: full_name, email_address, etc.
            if (supabaseClient) {
                const { data, error } = await supabaseClient
                    .from("inquiries")
                    .insert([payload]);

                // Handle Response
                if (error) {
                    console.error("Insert failed:", error);
                    // Provide detailed error feedback
                    let errorMessage = "Sorry, your message could not be sent. " + (error.message || "Unknown error");
                    if (error.details) errorMessage += "\nDetails: " + error.details;

                    alert(errorMessage);
                } else {
                    console.log("Insert succeeded:", data);
                    // SUCCESS MESSAGE:
                    alert("Your request has been sent to the team. We will contact you shortly.");
                    form.reset(); // Clear the form
                }
            } else {
                console.error("Supabase client not initialized.");
                alert("System Error: Database connection failed.");
            }
        });
    }
    // --- Supabase Integration for 'Contact Expert' Modal ---
    const expertForm = document.getElementById("expertContactForm");

    if (expertForm) {
        expertForm.addEventListener("submit", async (e) => {
            e.preventDefault(); // Stop page refresh

            // Collect form values from Expert Modal
            // Only send fields that exist in Supabase table: full_name, phone_number, company_name
            const payload = {
                full_name: document.getElementById('expert_full_name').value.trim(),
                phone_number: document.getElementById('expert_phone_number').value.trim(),
                company_name: document.getElementById('expert_company_name').value.trim()
            };

            // Insert into Supabase
            if (supabaseClient) {
                const { data, error } = await supabaseClient
                    .from("inquiries")
                    .insert([payload]);

                if (error) {
                    console.error("Insert failed:", error);
                    let errorMessage = "Sorry, your message could not be sent. " + (error.message || "Unknown error");
                    if (error.details) errorMessage += "\nDetails: " + error.details;
                    alert(errorMessage);
                } else {
                    console.log("Insert succeeded:", data);
                    alert("Your request has been sent to the team. We will contact you shortly.");
                    expertForm.reset();
                    // Optional: Close the modal
                    if (typeof closeContactModal === 'function') {
                        closeContactModal();
                    }
                }
            } else {
                console.error("Supabase client not initialized.");
                alert("System Error: Database connection failed.");
            }
        });
    }
});
