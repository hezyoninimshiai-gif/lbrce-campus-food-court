/**
 * API Client
 * ==========
 * Wrapper around fetch() for making API calls to the Flask backend.
 * Automatically includes the Authorization header when user is logged in.
 */

// ──────────────────────────────────────────────
// Base Fetch Wrapper
// ──────────────────────────────────────────────
// async function apiRequest(endpoint, options = {}) {
//     Steps:
//     1. Build full URL: API_URL + endpoint (e.g., '/menu/stalls')
//     2. Get access token from auth.js: getAccessToken()
//     3. Set default headers:
//        - 'Content-Type': 'application/json'
//        - If token exists: 'Authorization': 'Bearer <token>'
//     4. Merge with any custom headers from options
//     5. Call fetch(url, { method, headers, body, ...options })
//     6. Parse response as JSON
//     7. If response not ok (4xx/5xx), throw error with response body
//     8. Return parsed JSON data
// }

// ──────────────────────────────────────────────
// Convenience Methods
// ──────────────────────────────────────────────

// async function apiGet(endpoint) {
//     return apiRequest(endpoint, { method: 'GET' });
// }

// async function apiPost(endpoint, body) {
//     return apiRequest(endpoint, {
//         method: 'POST',
//         body: JSON.stringify(body)
//     });
// }

// async function apiPut(endpoint, body) {
//     return apiRequest(endpoint, {
//         method: 'PUT',
//         body: JSON.stringify(body)
//     });
// }

// async function apiDelete(endpoint) {
//     return apiRequest(endpoint, { method: 'DELETE' });
// }

// ──────────────────────────────────────────────
// API Endpoint Helpers (Optional convenience layer)
// ──────────────────────────────────────────────

// --- Menu ---
// const menuApi = {
//     getStalls: () => apiGet('/menu/stalls'),
//     getStallItems: (stallId, category) => {
//         let url = `/menu/stalls/${stallId}/items`;
//         if (category) url += `?category=${category}`;
//         return apiGet(url);
//     },
//     getItem: (itemId) => apiGet(`/menu/items/${itemId}`),
//     search: (query) => apiGet(`/menu/search?q=${encodeURIComponent(query)}`),
// };

// --- Orders ---
// const ordersApi = {
//     create: (stallId, items) => apiPost('/orders', { stall_id: stallId, items }),
//     list: (status) => {
//         let url = '/orders';
//         if (status) url += `?status=${status}`;
//         return apiGet(url);
//     },
//     get: (orderId) => apiGet(`/orders/${orderId}`),
// };

// --- User ---
// const userApi = {
//     getProfile: () => apiGet('/users/profile'),
//     updateProfile: (data) => apiPut('/users/profile', data),
// };

// --- Admin ---
// const adminApi = {
//     getPendingOrders: () => apiGet('/admin/orders/pending'),
//     getAllOrders: (status, date) => {
//         const params = new URLSearchParams();
//         if (status) params.set('status', status);
//         if (date) params.set('date', date);
//         const qs = params.toString();
//         return apiGet(`/admin/orders${qs ? '?' + qs : ''}`);
//     },
//     approveOrder: (orderId, estimatedTime) => apiPost(`/admin/orders/${orderId}/approve`, { estimated_time: estimatedTime }),
//     rejectOrder: (orderId, reason) => apiPost(`/admin/orders/${orderId}/reject`, { reason }),
//     markReady: (orderId) => apiPost(`/admin/orders/${orderId}/ready`),
//     completeOrder: (orderId) => apiPost(`/admin/orders/${orderId}/complete`),
//     addMenuItem: (data) => apiPost('/admin/menu/items', data),
//     updateMenuItem: (itemId, data) => apiPut(`/admin/menu/items/${itemId}`, data),
//     deleteMenuItem: (itemId) => apiDelete(`/admin/menu/items/${itemId}`),
//     getStats: () => apiGet('/admin/stats'),
// };
