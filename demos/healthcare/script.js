document.addEventListener('DOMContentLoaded', () => {
    // GSAP Scroll Animations
    gsap.registerPlugin(ScrollTrigger);

    // Hero Entry
    const heroTl = gsap.timeline();
    heroTl.from(".hero-content > *", {
        y: 30,
        opacity: 0,
        stagger: 0.1,
        duration: 1,
        ease: "power3.out"
    })
        .from(".animate-float", {
            scale: 0.9,
            opacity: 0,
            duration: 1,
            ease: "back.out(1.7)"
        }, "-=0.5");

    // Appointment Widget Hover
    const widget = document.querySelector('.fixed.bottom-8');
    if (widget) {
        widget.addEventListener('mouseenter', () => {
            gsap.to(widget, { scale: 1.1, duration: 0.3, ease: "back.out(1.7)" });
        });
        widget.addEventListener('mouseleave', () => {
            gsap.to(widget, { scale: 1, duration: 0.3 });
        });
    }

    // Interactive diagnosis button (Mock)
    const diagnosisBtn = document.querySelector('button.bg-blue-600');
    if (diagnosisBtn) {
        diagnosisBtn.addEventListener('click', () => {
            diagnosisBtn.innerHTML = '<span class="material-symbols-outlined animate-spin">refresh</span> Analyzing...';
            setTimeout(() => {
                diagnosisBtn.innerHTML = '<span class="material-symbols-outlined">check_circle</span> Analysis Complete';
                diagnosisBtn.classList.add('bg-green-600');
                diagnosisBtn.classList.remove('bg-blue-600');
            }, 2000);
        });
    }
});
