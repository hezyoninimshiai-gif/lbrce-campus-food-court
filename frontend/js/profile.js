/**
 * Profile Page Logic (profile.html)
 * ==================================
 * Loads and updates the authenticated user's profile.
 * Includes Telegram ID linking for notifications.
 */

// ──────────────────────────────────────────────
// On Page Load
// ──────────────────────────────────────────────
// document.addEventListener('DOMContentLoaded', async () => {
//     Steps:
//     1. Call requireLogin() — redirect if not authenticated
//     2. Call updateNavBar()
//     3. Call loadProfile() to populate the form
//     4. Setup form submit handler
// });

// ──────────────────────────────────────────────
// Load Profile
// ──────────────────────────────────────────────
// async function loadProfile() {
//     Steps:
//     1. Call userApi.getProfile() — GET /api/users/profile
//     2. If error, show error message
//     3. Populate form fields:
//        - Email (read-only text, not an input)
//        - Name input value
//        - Phone input value
//        - Telegram ID input value (may be null)
//        - Role badge (read-only)
// }

// ──────────────────────────────────────────────
// Save Profile
// ──────────────────────────────────────────────
// async function saveProfile(event) {
//     Steps:
//     1. event.preventDefault()
//     2. Get values from form: name, phone, telegram_id
//     3. Build update object with only changed/non-empty fields
//     4. Call userApi.updateProfile(data) — PUT /api/users/profile
//     5. If success: show success message/toast
//     6. If error: show error message
// }

// ──────────────────────────────────────────────
// Telegram Info Section
// ──────────────────────────────────────────────
// Display instructions for getting Telegram chat ID:
// 1. "To receive order notifications via Telegram:"
// 2. "Open Telegram and search for @userinfobot"
// 3. "Send /start to get your Chat ID"
// 4. "Enter the Chat ID number in the field above and save"
