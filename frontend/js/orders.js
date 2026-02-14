/**
 * Orders Page Logic (orders.html)
 * ================================
 * Displays the authenticated user's order history.
 * Supports filtering by status and auto-refresh.
 */

// ──────────────────────────────────────────────
// On Page Load
// ──────────────────────────────────────────────
// document.addEventListener('DOMContentLoaded', async () => {
//     Steps:
//     1. Call requireLogin() — redirect to login.html if not authenticated
//     2. Call updateNavBar()
//     3. Call loadOrders() to fetch and render orders
//     4. Setup status filter tab click handlers
//     5. Start auto-refresh interval (every 30 seconds)
// });

// ──────────────────────────────────────────────
// Load Orders
// ──────────────────────────────────────────────
// async function loadOrders(statusFilter = null) {
//     Steps:
//     1. Show loading spinner
//     2. Call ordersApi.list(statusFilter) — GET /api/orders?status=<filter>
//     3. If error, show error message
//     4. If empty, show "No orders yet" empty state
//     5. For each order, render an order card
//     6. Hide spinner
// }

// ──────────────────────────────────────────────
// Render Order Card
// ──────────────────────────────────────────────
// function renderOrderCard(order) {
//     Steps:
//     1. Create a Bootstrap card or accordion item:
//        - Order ID: "#123"
//        - Stall name
//        - Status badge (color-coded via Bootstrap classes):
//          pending → badge bg-warning
//          approved → badge bg-info
//          ready → badge bg-success
//          completed → badge bg-secondary
//          rejected → badge bg-danger
//        - Date/time: format order.created_at to readable string
//        - Total: "₹105"
//     2. Collapsible item list:
//        - "2x Masala Dosa — ₹80"
//        - "1x Vada (2 pcs) — ₹25"
//     3. If status === 'rejected': show rejection_reason in red
//     4. If status === 'approved' && estimated_time: show "Ready in ~15 minutes"
//     5. Return card HTML
// }

// ──────────────────────────────────────────────
// Status Filter Tabs
// ──────────────────────────────────────────────
// function setupFilterTabs() {
//     Steps:
//     1. Get all filter tab elements (All, Pending, Approved, Ready, Completed, Rejected)
//     2. Add click handler to each:
//        - Set active class on clicked tab
//        - Remove active from other tabs
//        - Call loadOrders(status) — 'All' passes null
// }

// ──────────────────────────────────────────────
// Auto-Refresh
// ──────────────────────────────────────────────
// let refreshInterval;
// function startAutoRefresh() {
//     refreshInterval = setInterval(() => {
//         loadOrders(currentFilter);  // re-fetch with current filter
//     }, 30000);  // every 30 seconds
// }

// ──────────────────────────────────────────────
// Format Date
// ──────────────────────────────────────────────
// function formatDate(dateString) {
//     Steps:
//     1. Parse dateString into Date object
//     2. Return formatted string: "15 Jan 2024, 10:30 AM"
//     3. Or use relative time: "5 minutes ago"
// }
