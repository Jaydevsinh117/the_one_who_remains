## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2025-05-24 - Accessibility of Cosmic Theme Controls
**Learning:** Icon-only buttons (common in the footer and chat widget) were completely invisible to screen readers and keyboard users. The "Cosmic" theme's dark/gold palette requires specific `focus-visible:ring-gold` styles to ensure focus states are visible against dark backgrounds without clashing.
**Action:** Always add `aria-label` to icon buttons and standard `focus-visible:ring-2 focus-visible:ring-gold` classes to interactive elements.
