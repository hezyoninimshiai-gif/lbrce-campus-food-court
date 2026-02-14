/**
 * Supabase Client Initialization
 * ===============================
 * Creates and exports the Supabase client instance.
 * Uses the Supabase JS library loaded via CDN in the HTML files.
 *
 * The CDN script tag <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 * makes `supabase` available as a global: window.supabase
 */

// ──────────────────────────────────────────────
// Initialize Supabase Client
// ──────────────────────────────────────────────
// Steps:
// 1. Use the global supabase object from the CDN
// 2. Call supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY)
// 3. Store the client in a variable for use across the app
//
// const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
//
// Note: The CDN exposes `supabase` as a global. We create `supabaseClient`
// to avoid naming conflicts.

// ──────────────────────────────────────────────
// Auth State Listener
// ──────────────────────────────────────────────
// Steps:
// 1. Listen for auth state changes (login/logout)
// 2. supabaseClient.auth.onAuthStateChange((event, session) => { ... })
// 3. On SIGNED_IN: store session, update UI (show/hide nav links)
// 4. On SIGNED_OUT: clear session, redirect to login if on protected page
