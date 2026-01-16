## 2026-01-16 - Audio Playback UX
**Learning:** Audio playback that doesn't self-manage (stopping previous tracks) leads to chaotic user experience. Users expect a "toggle" interaction (Play/Pause) rather than just "Play", and immediate visual feedback of the active state.
**Action:** Always implement a global audio manager for media playback to prevent overlapping sounds, and provide clear visual state indicators (swapping Play/Pause icons) on the control element itself.
