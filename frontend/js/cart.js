/**
 * Cart Logic (cart.js)
 * ====================
 * Manages the shopping cart using localStorage.
 * Used by both menu.html (adding items) and cart.html (viewing/placing order).
 */

// ──────────────────────────────────────────────
// Constants
// ──────────────────────────────────────────────
// const CART_KEY = 'lbrce_cart';
// Cart format in localStorage:
// {
//   stall_id: 1,
//   stall_name: "South Indian Corner",
//   items: [
//     { menu_item_id: 1, name: "Masala Dosa", price: 40, quantity: 2, image_url: "" },
//     { menu_item_id: 3, name: "Vada (2 pcs)", price: 25, quantity: 1, image_url: "" }
//   ]
// }

// ──────────────────────────────────────────────
// Get Cart
// ──────────────────────────────────────────────
// function getCart() {
//     Steps:
//     1. Read CART_KEY from localStorage
//     2. If null, return { stall_id: null, stall_name: '', items: [] }
//     3. Parse JSON and return
// }

// ──────────────────────────────────────────────
// Save Cart
// ──────────────────────────────────────────────
// function saveCart(cart) {
//     Steps:
//     1. JSON.stringify(cart)
//     2. localStorage.setItem(CART_KEY, jsonString)
// }

// ──────────────────────────────────────────────
// Add to Cart
// ──────────────────────────────────────────────
// function addToCart(item, stallId, stallName) {
//     Steps:
//     1. Get current cart
//     2. If cart has items from a DIFFERENT stall:
//        - Show confirm dialog: "Your cart has items from another stall. Clear cart?"
//        - If yes: clear cart and continue
//        - If no: return (don't add)
//     3. Set cart.stall_id and cart.stall_name
//     4. Check if item already exists in cart (by menu_item_id)
//        - If exists: increment quantity
//        - If not: add new item { menu_item_id, name, price, quantity: 1, image_url }
//     5. Save cart
// }

// ──────────────────────────────────────────────
// Update Quantity
// ──────────────────────────────────────────────
// function updateQuantity(menuItemId, newQuantity) {
//     Steps:
//     1. Get cart
//     2. Find item by menu_item_id
//     3. If newQuantity <= 0: remove item from cart
//     4. Else: update quantity
//     5. If cart.items is now empty: clear cart entirely
//     6. Save cart
// }

// ──────────────────────────────────────────────
// Remove from Cart
// ──────────────────────────────────────────────
// function removeFromCart(menuItemId) {
//     Steps:
//     1. Get cart
//     2. Filter out the item with matching menu_item_id
//     3. If cart.items is now empty: clear cart
//     4. Save cart
// }

// ──────────────────────────────────────────────
// Clear Cart
// ──────────────────────────────────────────────
// function clearCart() {
//     localStorage.removeItem(CART_KEY);
// }

// ──────────────────────────────────────────────
// Get Cart Total
// ──────────────────────────────────────────────
// function getCartTotal() {
//     Steps:
//     1. Get cart
//     2. Sum up (price * quantity) for each item
//     3. Return total
// }

// ──────────────────────────────────────────────
// Get Cart Item Count
// ──────────────────────────────────────────────
// function getCartItemCount() {
//     Steps:
//     1. Get cart
//     2. Sum up quantities of all items
//     3. Return count
// }

// ──────────────────────────────────────────────
// Render Cart Page (cart.html only)
// ──────────────────────────────────────────────
// function renderCartPage() {
//     Steps:
//     1. Get cart
//     2. If cart is empty:
//        - Show "Your cart is empty" message
//        - Show "Browse Stalls" link
//        - Hide cart summary
//        - Return
//     3. Show stall name header
//     4. For each item, render a cart row:
//        - Item name, image thumbnail
//        - Price per unit
//        - Quantity controls: [-] [qty] [+]
//        - Subtotal
//        - Remove button
//     5. Render cart summary:
//        - Total items
//        - Total amount
//        - "Place Order" button
//     6. Attach event handlers to quantity buttons and remove buttons
// }

// ──────────────────────────────────────────────
// Place Order
// ──────────────────────────────────────────────
// async function placeOrder() {
//     Steps:
//     1. Check if user is logged in — if not, redirect to login.html
//     2. Get cart
//     3. Build API request body:
//        { stall_id: cart.stall_id, items: cart.items.map(i => ({ menu_item_id: i.menu_item_id, quantity: i.quantity })) }
//     4. Call ordersApi.create(stallId, items) — POST /api/orders
//     5. If success:
//        - Clear cart
//        - Show success message/toast
//        - Redirect to orders.html
//     6. If error:
//        - Show error message (e.g., "Item no longer available")
// }
