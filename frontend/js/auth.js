/**
 * Auth Helpers
 * ============
 * Functions for login, register, logout, and auth state checks.
 * Uses the Supabase client from supabase.js.
 */

// ──────────────────────────────────────────────
// Login
// ──────────────────────────────────────────────
// async function loginUser(email, password) {
//     Steps:
//     1. Call supabaseClient.auth.signInWithPassword({ email, password })
//     2. If error, throw or return the error
//     3. If success, the session is auto-stored by Supabase JS client
//     4. Return the session data
// }

// ──────────────────────────────────────────────
// Register
// ──────────────────────────────────────────────
// async function registerUser(email, password, name, phone) {
//     Steps:
//     1. Call supabaseClient.auth.signUp({ email, password })
//     2. If error, throw or return the error
//     3. Get the user ID from the signup response
//     4. Call API to create profile: POST /api/auth/register with { email, name, phone }
//        (or insert directly into users table via Supabase client)
//     5. Return session data
// }

// ──────────────────────────────────────────────
// Logout
// ──────────────────────────────────────────────
// async function logoutUser() {
//     Steps:
//     1. Call supabaseClient.auth.signOut()
//     2. Clear any local state
//     3. Redirect to login.html
// }

// ──────────────────────────────────────────────
// Get Current Session
// ──────────────────────────────────────────────
// async function getCurrentSession() {
//     Steps:
//     1. Call supabaseClient.auth.getSession()
//     2. Return session object (or null if not logged in)
// }

// ──────────────────────────────────────────────
// Get Current User
// ──────────────────────────────────────────────
// async function getCurrentUser() {
//     Steps:
//     1. Call supabaseClient.auth.getUser()
//     2. Return user object (or null)
// }

// ──────────────────────────────────────────────
// Get Access Token
// ──────────────────────────────────────────────
// async function getAccessToken() {
//     Steps:
//     1. Get current session
//     2. Return session.access_token (used in Authorization header for API calls)
//     3. If no session, return null
// }

// ──────────────────────────────────────────────
// Auth Guard
// ──────────────────────────────────────────────
// async function requireLogin() {
//     Steps:
//     1. Check if user is logged in (getCurrentSession)
//     2. If not logged in, redirect to login.html
//     3. Return user data if logged in
// }

// ──────────────────────────────────────────────
// Admin Guard
// ──────────────────────────────────────────────
// async function requireAdmin() {
//     Steps:
//     1. Call requireLogin() first
//     2. Get user profile from API: GET /api/users/profile
//     3. Check if role === 'admin'
//     4. If not admin, redirect to index.html
//     5. Return user profile data
// }

// ──────────────────────────────────────────────
// Update Nav Bar
// ──────────────────────────────────────────────
// function updateNavBar(user) {
//     Steps:
//     1. If user is logged in:
//        - Show: My Orders, Profile, Logout links
//        - Hide: Login/Register link
//        - If user.role === 'admin': show Admin link
//     2. If user is NOT logged in:
//        - Show: Login/Register link
//        - Hide: My Orders, Profile, Logout, Admin links
// }
