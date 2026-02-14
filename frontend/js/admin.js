/**
 * Admin Dashboard Logic (admin.html)
 * ====================================
 * Displays stats, pending orders, and recent order management.
 * Requires admin role.
 */

// ──────────────────────────────────────────────
// On Page Load
// ──────────────────────────────────────────────
// document.addEventListener('DOMContentLoaded', async () => {
//     Steps:
//     1. Call requireAdmin() — redirect if not admin
//     2. Call updateNavBar()
//     3. Call loadStats() to populate stat cards
//     4. Call loadPendingOrders()
//     5. Call loadRecentOrders()
//     6. Start auto-refresh for pending orders (every 15 seconds)
// });

// ──────────────────────────────────────────────
// Load Stats
// ──────────────────────────────────────────────
// async function loadStats() {
//     Steps:
//     1. Call adminApi.getStats() — GET /api/admin/stats
//     2. Update stat cards:
//        - Today's Orders count
//        - Pending Orders count (highlight if > 0)
//        - Today's Revenue (₹ formatted)
//        - Top popular item name and count
// }

// ──────────────────────────────────────────────
// Load Pending Orders
// ──────────────────────────────────────────────
// async function loadPendingOrders() {
//     Steps:
//     1. Call adminApi.getPendingOrders() — GET /api/admin/orders/pending
//     2. If empty, show "No pending orders" message
//     3. For each order, render a pending order card with:
//        - Student name and phone
//        - Stall name
//        - Items list with quantities
//        - Total amount
//        - Time ago (relative time from created_at)
//        - "Approve" button (green)
//        - "Reject" button (red)
//     4. Attach click handlers to approve/reject buttons
// }

// ──────────────────────────────────────────────
// Approve Order
// ──────────────────────────────────────────────
// async function approveOrder(orderId) {
//     Steps:
//     1. Show Bootstrap modal with estimated time input (default: 15 minutes)
//     2. On confirm:
//        a. Call adminApi.approveOrder(orderId, estimatedTime)
//        b. If success: close modal, remove card from pending list, show toast, refresh stats
//        c. If error: show error in modal
// }

// ──────────────────────────────────────────────
// Reject Order
// ──────────────────────────────────────────────
// async function rejectOrder(orderId) {
//     Steps:
//     1. Show Bootstrap modal with reason textarea (required)
//     2. On confirm:
//        a. Validate reason is not empty
//        b. Call adminApi.rejectOrder(orderId, reason)
//        c. If success: close modal, remove card from pending list, show toast, refresh stats
//        d. If error: show error in modal
// }

// ──────────────────────────────────────────────
// Load Recent Orders (Table)
// ──────────────────────────────────────────────
// async function loadRecentOrders() {
//     Steps:
//     1. Call adminApi.getAllOrders() — today's orders
//     2. Render a Bootstrap table with columns:
//        Order ID | Student | Stall | Amount | Status (badge) | Time | Actions
//     3. Actions column:
//        - If status === 'approved': "Mark Ready" button
//        - If status === 'ready': "Complete" button
//        - Otherwise: no action buttons
//     4. Attach click handlers to action buttons
// }

// ──────────────────────────────────────────────
// Mark Ready / Complete
// ──────────────────────────────────────────────
// async function markOrderReady(orderId) {
//     Steps:
//     1. Call adminApi.markReady(orderId)
//     2. Refresh recent orders table
//     3. Show toast
// }

// async function completeOrder(orderId) {
//     Steps:
//     1. Call adminApi.completeOrder(orderId)
//     2. Refresh recent orders table
//     3. Show toast
// }

// ──────────────────────────────────────────────
// Auto-Refresh
// ──────────────────────────────────────────────
// setInterval(() => {
//     loadPendingOrders();
//     loadStats();
// }, 15000);
