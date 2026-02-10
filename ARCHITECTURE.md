# ARCHITECTURE

## Tech Stack
- **Frontend Core:** HTML5, JavaScript (Vanilla + ES6 Modules).
- **Styling:** Tailwind CSS (CDN/Utility-first) + Custom CSS (`style.css`).
- **3D & Graphics:** Spline Design (`@splinetool/viewer`).
- **Animations:** GSAP (GreenSock Animation Platform) + ScrollTrigger, Lenis (Smooth Scrolling), Typed.js.
- **Icons & Fonts:** Google Fonts (Outfit, Space Grotesk), Material Symbols Outlined, FontAwesome.
- **Backend/Database:** Supabase (PostgreSQL) via `@supabase/supabase-js`.

## Project Structure
```
/auratekk
├── index.html          # Main entry point (Dark Mode default)
├── light.html          # Light Mode version
├── script.js           # Core logic (Animations, Form Handling, Theme Switching)
├── style.css           # Custom styles and overrides
├── midnight.html       # Standalone Dark Mode Demo
├── daylight.html       # Standalone Light Mode Demo
└── assets/             # Images, SVGs, and Icons
```

## Data Flow
1. **User Interaction:** User submits a contact form (Main or Expert Modal).
2. **Client-Side Processing:** `script.js` captures input, validates fields.
3. **API Request:** Supabase JS Client sends an `insert` request to the `inquiries` table.
4. **Feedback:** UI updates with success/error messages based on the promise resolution.

## Key Components
- **Hero Section:** interactive 3D viewer + value proposition.
- **Service Cards:** Hover-responsive cards with modal details.
- **Project Ecosystem:** Links to standalone demo pages.
- **Contact Forms:** Two variants (General & Expert) sharing Supabase logic.
