# REQUIREMENTS

## Functional Requirements
- **Theme Switching:** Users must be able to toggle between Dark and Light modes seamlessly.
- **Navigation:** Smooth scroll to sections; reliable external links to demo pages.
- **Form Submission:** 
  - Capture Name, Email, Phone, Company, Project Interest.
  - Store data in Supabase `inquiries` table.
  - Show immediate success/error feedback.
  - Prevent page reload on submission.
- **Responsiveness:** Fully adaptive layout for Mobile, Tablet, and Desktop.
- **Performance:** Preloader to handle asset loading; optimization for 3D elements.

## Non-Functional Requirements
- **Aesthetics:** Futuristic, premium, high-contrast design.
- **Performance:** Smooth 60fps animations; fast initial load time.
- **Usability:** Intuitive navigation; clear calls to action (CTAs).
- **Code Quality:** Modular JavaScript; clean HTML structure; tailored Tailwind classes.

## External Dependencies
- Tailwind CSS (CDN)
- GSAP & ScrollTrigger (CDN)
- Spline Viewer (Module)
- Supabase SDK (CDN)
- Lenis (CDN)
