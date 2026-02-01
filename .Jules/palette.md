## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2025-05-20 - Icon-Only Button Accessibility
**Learning:** The application frequently uses icon-only buttons (Chatbot, Socials, Menu) without accessible labels, relying on visual context which excludes screen reader users.
**Action:** Ensure all icon-only interactive elements receive an explicit aria-label or sr-only text.
