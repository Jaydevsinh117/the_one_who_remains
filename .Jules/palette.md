## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2025-05-21 - Systemic Missing Accessible Names
**Learning:** The base template frequently uses icon-only buttons (Feather icons) for primary navigation and social links without accessible names. This renders major parts of the site navigation invisible to screen readers.
**Action:** Systematically check all elements containing `<i data-feather="...">` for `aria-label` or surrounding text content during reviews.
