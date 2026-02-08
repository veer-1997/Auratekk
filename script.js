
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

    // --- 3D Hero Scene Implementation ---
    const heroScene = initHeroScene();

    // Initial Theme Update for 3D Scene
    if (heroScene) {
        heroScene.updateTheme(html.classList.contains('dark'));
    }

    // --- Loading Screen Logic ---
    const loader = document.getElementById('loader-overlay');
    if (loader) {
        // Wait for animations to finish (approx 2.5s + buffer)
        setTimeout(() => {
            loader.classList.add('animate-slide-up');

            // Remove from DOM after slide-up animation
            setTimeout(() => {
                loader.remove();
                document.body.classList.remove('overflow-hidden');
            }, 800);
        }, 2800);
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

// --- Industry Modal Functions ---
function openIndustryModal(industryId) {
    const modal = document.getElementById('industryModal');
    const allContent = document.querySelectorAll('.industry-content');
    const targetContent = document.getElementById(`modal-${industryId}`);

    // Hide all industry content
    allContent.forEach(content => content.classList.add('hidden'));

    // Show target industry content
    if (targetContent) {
        targetContent.classList.remove('hidden');
    }

    // Show modal with animation
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

function closeIndustryModal() {
    const modal = document.getElementById('industryModal');

    // Animate out
    modal.style.opacity = '0';
    modal.style.transform = 'scale(0.95)';

    setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }, 300);
}

// Close modal on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeIndustryModal();
        closeServiceModal();
    }
});

// --- Service Modal Functions ---
function openServiceModal(serviceId) {
    const modal = document.getElementById('serviceModal');
    const allContent = document.querySelectorAll('#serviceModal .service-content');
    const targetContent = document.getElementById(`service-${serviceId}`);

    // Hide all service content
    allContent.forEach(content => content.classList.add('hidden'));

    // Show target service content
    if (targetContent) {
        targetContent.classList.remove('hidden');
    }

    // Show modal with animation
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

function closeServiceModal() {
    const modal = document.getElementById('serviceModal');

    // Animate out
    modal.style.opacity = '0';
    modal.style.transform = 'scale(0.95)';

    setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }, 300);
}

function navigateService(direction) {
    const allContent = Array.from(document.querySelectorAll('#serviceModal .service-content'));
    let currentIndex = allContent.findIndex(content => !content.classList.contains('hidden'));

    if (currentIndex === -1) return; // Should not happen if modal is open

    let newIndex;
    if (direction === 'next') {
        newIndex = (currentIndex + 1) % allContent.length;
    } else {
        newIndex = (currentIndex - 1 + allContent.length) % allContent.length;
    }

    // Hide current
    allContent[currentIndex].classList.add('hidden');

    // Show new
    allContent[newIndex].classList.remove('hidden');

    // Optional: Add a simple fade animation for the transition
    const newContent = allContent[newIndex];
    newContent.style.opacity = '0';
    newContent.style.transform = 'translateX(' + (direction === 'next' ? '20px' : '-20px') + ')';

    requestAnimationFrame(() => {
        newContent.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        newContent.style.opacity = '1';
        newContent.style.transform = 'translateX(0)';
    });
}

// --- Contact Modal Logic ---
function openContactModal() {
    const modal = document.getElementById('contactModal');
    if (!modal) return;

    modal.classList.remove('hidden');
    modal.classList.add('flex');

    document.body.style.overflow = 'hidden';
}

function closeContactModal() {
    const modal = document.getElementById('contactModal');
    if (!modal) return;

    modal.classList.add('hidden');
    modal.classList.remove('flex');

    document.body.style.overflow = '';
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
// Note: REPLACE 'YOUR_SUPABASE_URL_HERE' with your actual Supabase Project URL
const SUPABASE_URL = 'YOUR_SUPABASE_URL_HERE';
const SUPABASE_ANON_KEY = 'sb_publishable_V6BPhOMhOj2-kIM58jqcqQ_TPLNgPmU'; // User provided key

// Initialize Client (will fail without valid URL, so we wrap it or handle it)
let supabaseClient = null;
if (typeof supabase !== 'undefined' && SUPABASE_URL !== 'YOUR_SUPABASE_URL_HERE') {
    try {
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } catch (e) {
        console.error('Supabase Initialization Error:', e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const mainForm = document.getElementById('mainContactForm');

    if (mainForm) {
        mainForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Stop page refresh

            // Collect Data
            const formData = {
                name: document.getElementById('contactName')?.value,
                email: document.getElementById('contactEmail')?.value,
                phone: document.getElementById('contactPhone')?.value,
                company: document.getElementById('contactCompany')?.value,
                interest: document.getElementById('contactProject')?.value,
                submitted_at: new Date().toISOString()
            };

            console.log('Form Data Collected:', formData);

            // Supabase Submission
            if (supabaseClient) {
                const { data, error } = await supabaseClient
                    .from('leads') // Assuming table name 'leads'
                    .insert([formData]);

                if (error) {
                    console.error('Supabase Error:', error);
                    alert('Error sending message: ' + error.message);
                } else {
                    console.log('Supabase Success:', data);
                    alert('Message transmitted successfully. We will be in touch.');
                    mainForm.reset();
                }
            } else {
                console.warn('Supabase not initialized. Missing URL.');
                alert('Simulation: Message received! (Supabase URL pending: Please provide Project URL)');
                mainForm.reset();
            }
        });
    }
});
