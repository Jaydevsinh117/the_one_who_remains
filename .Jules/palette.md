## 2025-05-20 - Cosmic Theme Contrast & Simulated Feedback
**Learning:** The "Cosmic" theme relies heavily on transparent backgrounds (`bg-white/10`) with Gold text, which often fails WCAG contrast standards. Additionally, missing backend endpoints (like `/subscribe`) can break the experience; simulated feedback (mock success) is a superior interim UX pattern to maintain immersion.
**Action:** When working with the Cosmic theme, verify contrast against the specific background gradient. Use the `handleSubscription` simulation pattern for forms where backend logic is pending.

## 2025-05-20 - Deceptive State Simulation
**Learning:** Simulating a "Playing" state (showing a stop button + timer) when the audio file is actually missing (404) is deceptive UX. It leads users to debug their own hardware/volume settings unnecessarily.
**Action:** If an asset is missing or fails to load, provide honest feedback (e.g., "Unavailable" or disabled state) rather than simulating a successful interaction.
