# CONSTRAINTS

## Technical Constraints
- **Hosting:** Must be compatible with static hosting environments (Netlify, Vercel, GitHub Pages).
- **Supabase:** Dependent on free-tier limits of Supabase for database operations.
- **Browser Capability:** Heavy use of WebGL (Spline) requires modern browsers (Chrome, Firefox, Safari, Edge) with hardware acceleration.
- **CDN Dependency:** Project relies on CDN links for libraries; offline development requires internet access or local downloads of libs.

## Design Constraints
- **Typography:** Limited to 'Outfit' and 'Space Grotesk' to maintain brand identity.
- **Color Palette:** Strictly defined in Tailwind config (accent-gold, accent-purple, etc.) - no arbitrary colors.
- **3D Performance:** Scene complexity must be managed to allow loading on mobile devices within 3-5 seconds.

## Compliance & Security
- **Data Privacy:** Basic collection of PII (Name, Email, Phone); requires GDPR/CCPA consideration if scaling.
- **Public API Keys:** Supabase Anon Key is exposed client-side; strictly reliant on Row Level Security (RLS) for protection.
