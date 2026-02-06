## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2026-05-21 - Animation Pausing & Icon Labels
**Learning:** The "Cosmic" theme's floating animations (e.g., `animate-float`) on interactive elements like the chatbot toggle can cause click target instability and motion sickness.
**Action:** Always apply `hover:animate-none` and `focus:animate-none` to any interactive element using continuous animation. Ensure all icon-only buttons (socials, mobile menu) have explicit `aria-label`s as they are consistently missing.
