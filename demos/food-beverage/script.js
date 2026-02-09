document.addEventListener('DOMContentLoaded', () => {
    gsap.registerPlugin(ScrollTrigger);

    // Hero Animations
    const heroTl = gsap.timeline();

    heroTl.from(".reveal-hero", {
        y: 50,
        opacity: 0,
        duration: 1.5,
        stagger: 0.2,
        ease: "power3.out"
    });

    heroTl.from("header img", {
        scale: 1,
        duration: 2,
        ease: "power2.out"
    }, 0);

    // Scroll Animations for Sections
    const scrollElements = document.querySelectorAll('[data-scroll]');

    scrollElements.forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 80%",
                toggleActions: "play none none reverse"
            },
            y: 40,
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });

    // Menu Item Hover Effect (Parallaxish)
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const { left, top, width, height } = item.getBoundingClientRect();
            const x = (e.clientX - left) / width - 0.5;
            const y = (e.clientY - top) / height - 0.5;

            gsap.to(item.querySelector('img'), {
                x: x * 20,
                y: y * 20,
                scale: 1.15,
                duration: 0.5
            });
        });

        item.addEventListener('mouseleave', () => {
            gsap.to(item.querySelector('img'), {
                x: 0,
                y: 0,
                scale: 1, // Reset to CSS hover scale handled by CSS or 1
                duration: 0.5
            });
        });
    });
});
