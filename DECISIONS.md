# DECISIONS

## 2026-02-09: Architecture Documentation Strategy
- **Context:** The project lacked centralized documentation, making it harder to track changes and architecture.
- **Decision:** Implemented a standard documentation suite (`CONTEXT.md`, `ARCHITECTURE.md`, etc.) in the project root.
- **Goal:** To serve as a single source of truth for AI agents and developers.

## 2026-02-09: Removal of Ecosystem Pages
- **Context:** The "Live Ecosystem" and distinct demo pages (`midnight.html`, `daylight.html`) were deemed unnecessary by the user after implementation.
- **Decision:** Completely remove these files and revert the navigation.
- **Reasoning:** Simplified project scope; user preference.

## 2026-02-08: Supabase for Backend
- **Context:** Need for a lightweight, scalable backend for form submissions without managing a full server.
- **Decision:** Use Supabase with client-side JS SDK.
- **Trade-off:** Exposes Anon Key (mitigated by RLS policies).

## 2026-02-08: Tailwind CSS Utilization
- **Context:** Need for rapid styling and consistent design tokens.
- **Decision:** Use Tailwind CSS via CDN for development speed, with a custom configuration inject in the `<head>`.
- **Note:** For production, a build step to purge unused CSS would be ideal, but CDN is sufficient for current prototype phase.
