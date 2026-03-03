## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2025-05-21 - Accessible Form Feedback
**Learning:** Using `window.alert()` for form feedback disrupts the user flow and is inaccessible to screen readers.
**Action:** Replace alerts with inline status containers using `aria-live="polite"`. Ensure submit buttons have visual loading states to prevent double-submission.
