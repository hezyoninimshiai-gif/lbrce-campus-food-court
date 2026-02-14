/**
 * Admin Menu Management Logic (admin-menu.html)
 * ==============================================
 * Manages menu items: add, edit, delete, toggle availability.
 * Includes image upload to Supabase Storage.
 * Requires admin role.
 */

// ──────────────────────────────────────────────
// On Page Load
// ──────────────────────────────────────────────
// document.addEventListener('DOMContentLoaded', async () => {
//     Steps:
//     1. Call requireAdmin() — redirect if not admin
//     2. Call updateNavBar()
//     3. Call loadStalls() to populate stall selector dropdown
//     4. Setup stall selector change handler
//     5. Setup "Add Menu Item" button click handler
//     6. Load items for the first stall by default
// });

// ──────────────────────────────────────────────
// Load Stalls Dropdown
// ──────────────────────────────────────────────
// async function loadStalls() {
//     Steps:
//     1. Call menuApi.getStalls()
//     2. Populate <select> dropdown with stall options
//     3. Select the first stall by default
//     4. Trigger loading items for the first stall
// }

// ──────────────────────────────────────────────
// Load Menu Items for Selected Stall
// ──────────────────────────────────────────────
// async function loadMenuItems(stallId) {
//     Steps:
//     1. Show loading state in items table
//     2. Call menuApi.getStallItems(stallId) — gets ALL items (including unavailable for admin)
//     3. Render items in a Bootstrap table:
//        Columns: Image | Name | Category | Price | Available | Actions
//     4. Image column: show thumbnail (50x50) or placeholder
//     5. Available column: toggle switch/checkbox
//     6. Actions column: Edit button, Delete button
//     7. Attach event handlers
// }

// ──────────────────────────────────────────────
// Open Add/Edit Modal
// ──────────────────────────────────────────────
// function openItemModal(item = null) {
//     Steps:
//     1. If item is null: "Add" mode — clear form, set title "Add Menu Item"
//     2. If item provided: "Edit" mode — pre-fill form, set title "Edit Menu Item"
//     3. Pre-fill fields:
//        - Name, Description, Price, Category (dropdown), Image preview
//     4. Setup image file input change handler (preview selected image)
//     5. Show the Bootstrap modal
// }

// ──────────────────────────────────────────────
// Upload Image to Supabase Storage
// ──────────────────────────────────────────────
// async function uploadImage(file) {
//     Steps:
//     1. Generate unique filename: `${Date.now()}-${file.name}`
//     2. Upload to Supabase Storage:
//        const { data, error } = await supabaseClient.storage
//            .from(STORAGE_BUCKET)
//            .upload(filename, file);
//     3. If error, throw or return error
//     4. Get public URL:
//        const { data: urlData } = supabaseClient.storage
//            .from(STORAGE_BUCKET)
//            .getPublicUrl(data.path);
//     5. Return urlData.publicUrl
// }

// ──────────────────────────────────────────────
// Save Item (Add or Edit)
// ──────────────────────────────────────────────
// async function saveItem(event) {
//     Steps:
//     1. event.preventDefault()
//     2. Get form values: name, description, price, category
//     3. Get the image file input
//     4. Let image_url = existingImageUrl (for edit mode)
//     5. If a new image file was selected:
//        a. Show upload spinner/progress
//        b. image_url = await uploadImage(file)
//        c. If upload fails, show error and return
//     6. Build request body: { stall_id, name, description, price, category, image_url }
//     7. If adding (no item ID):
//        Call adminApi.addMenuItem(data)
//     8. If editing (has item ID):
//        Call adminApi.updateMenuItem(itemId, data)
//     9. On success: close modal, refresh items table, show toast
//     10. On error: show error message in modal
// }

// ──────────────────────────────────────────────
// Delete Item
// ──────────────────────────────────────────────
// async function deleteItem(itemId) {
//     Steps:
//     1. Show confirmation dialog: "Are you sure you want to delete this item?"
//     2. If confirmed:
//        a. Call adminApi.deleteMenuItem(itemId)
//        b. Refresh items table
//        c. Show toast
// }

// ──────────────────────────────────────────────
// Toggle Availability
// ──────────────────────────────────────────────
// async function toggleAvailability(itemId, currentState) {
//     Steps:
//     1. Call adminApi.updateMenuItem(itemId, { is_available: !currentState })
//     2. Update the toggle switch UI
//     3. Show brief toast: "Item updated"
// }

// ──────────────────────────────────────────────
// Image Preview
// ──────────────────────────────────────────────
// function previewImage(fileInput, previewElement) {
//     Steps:
//     1. Listen for 'change' event on file input
//     2. If file selected:
//        a. Create FileReader
//        b. reader.onload = () => { previewElement.src = reader.result }
//        c. reader.readAsDataURL(file)
//     3. If no file: show existing image or placeholder
// }
