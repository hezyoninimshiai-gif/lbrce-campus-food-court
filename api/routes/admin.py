"""
Admin Routes
============
Blueprint: admin_bp
Prefix: /api/admin

Handles admin operations: order management, menu management, stats.
All endpoints require authentication AND admin role.
"""

# from flask import Blueprint, request, jsonify
# from middleware.auth_middleware import require_auth, require_admin
# from services.supabase_service import get_supabase_client
# from services.telegram import send_order_notification_to_student

# admin_bp = Blueprint("admin", __name__)


# ──────────────────────────────────────────────
# Order Management
# ──────────────────────────────────────────────


def get_pending_orders():
    """
    GET /api/admin/orders/pending

    List all orders with status='pending'.

    Headers: Authorization (admin only)

    Steps:
    1. Use @require_admin decorator to verify JWT and check role = 'admin'
    2. Query orders table:
       - SELECT o.*, u.name as user_name, u.phone as user_phone, fs.name as stall_name
         FROM orders o
         JOIN users u ON o.user_id = u.id
         JOIN food_stalls fs ON o.stall_id = fs.id
         WHERE o.status = 'pending'
         ORDER BY o.created_at ASC
    3. For each order, fetch order_items with menu_item details
    4. Return list of pending orders with user and stall info

    Response: [ { "id": 123, "user": {"name": "...", "phone": "..."}, "stall": {...}, "items": [...], ... } ]
    """
    pass


def get_all_orders():
    """
    GET /api/admin/orders

    List all orders with optional filters.

    Headers: Authorization (admin only)
    Query Params:
        - ?status=approved (optional)
        - ?date=2024-01-15 (optional)

    Steps:
    1. Use @require_admin decorator
    2. Get status and date query params
    3. Build query with optional filters
    4. Return filtered orders with user and stall info

    Response: [ { ...orders... } ]
    """
    pass


def approve_order(order_id):
    """
    POST /api/admin/orders/<order_id>/approve

    Approve a pending order.

    Headers: Authorization (admin only)
    URL Params: order_id (int)
    Body: { "estimated_time": 15 } (optional, minutes)

    Steps:
    1. Use @require_admin decorator
    2. Get order by ID — verify it exists and status is 'pending'
    3. If not pending, return 400 "Order is not in pending state"
    4. Update order: SET status = 'approved', estimated_time = :estimated_time, updated_at = NOW()
    5. Get user's telegram_id from users table
    6. If telegram_id exists, call send_order_notification_to_student():
       "Your order #123 has been approved! It will be ready in 15 minutes."
    7. Return updated order

    Response: { "order": {...}, "message": "Order approved" }
    """
    pass


def reject_order(order_id):
    """
    POST /api/admin/orders/<order_id>/reject

    Reject a pending order with a reason.

    Headers: Authorization (admin only)
    URL Params: order_id (int)
    Body: { "reason": "Item not available" }

    Steps:
    1. Use @require_admin decorator
    2. Get order by ID — verify it exists and status is 'pending'
    3. Parse JSON body — get reason
    4. Update order: SET status = 'rejected', rejection_reason = :reason, updated_at = NOW()
    5. Get user's telegram_id
    6. If telegram_id exists, send notification:
       "Your order #123 was rejected. Reason: Item not available."
    7. Return updated order

    Response: { "order": {...}, "message": "Order rejected" }
    """
    pass


def mark_ready(order_id):
    """
    POST /api/admin/orders/<order_id>/ready

    Mark an approved order as ready for pickup.

    Headers: Authorization (admin only)
    URL Params: order_id (int)

    Steps:
    1. Use @require_admin decorator
    2. Get order by ID — verify status is 'approved'
    3. Update order: SET status = 'ready', updated_at = NOW()
    4. Get user's telegram_id and stall name
    5. If telegram_id exists, send notification:
       "Your order #123 is ready for pickup at South Indian Corner!"
    6. Return updated order

    Response: { "order": {...}, "message": "Order marked as ready" }
    """
    pass


def complete_order(order_id):
    """
    POST /api/admin/orders/<order_id>/complete

    Mark an order as completed (picked up by student).

    Headers: Authorization (admin only)
    URL Params: order_id (int)

    Steps:
    1. Use @require_admin decorator
    2. Get order by ID — verify status is 'ready'
    3. Update order: SET status = 'completed', updated_at = NOW()
    4. Return updated order

    Response: { "order": {...}, "message": "Order completed" }
    """
    pass


# ──────────────────────────────────────────────
# Menu Management
# ──────────────────────────────────────────────


def add_menu_item():
    """
    POST /api/admin/menu/items

    Add a new menu item.

    Headers: Authorization (admin only)
    Body:
        {
            "stall_id": 1,
            "name": "Paneer Dosa",
            "description": "Dosa with paneer filling",
            "price": 60.00,
            "category": "main",
            "image_url": "https://xyz.supabase.co/storage/v1/object/public/menu-images/paneer-dosa.jpg"
        }

    Note: image_url comes from frontend after uploading to Supabase Storage.
    The API does NOT handle file uploads — it just stores the URL string.

    Steps:
    1. Use @require_admin decorator
    2. Parse JSON body
    3. Validate required fields: stall_id, name, price, category
    4. Validate stall_id exists
    5. Validate category is one of: 'main', 'snack', 'beverage', 'dessert'
    6. Insert into menu_items table
    7. Return created item with 201

    Response: { "item": {...} }
    """
    pass


def update_menu_item(item_id):
    """
    PUT /api/admin/menu/items/<item_id>

    Update an existing menu item.

    Headers: Authorization (admin only)
    URL Params: item_id (int)
    Body (all fields optional):
        {
            "name": "Updated Name",
            "price": 70.00,
            "is_available": false,
            "image_url": "https://..."
        }

    Steps:
    1. Use @require_admin decorator
    2. Get item by ID — verify it exists
    3. Parse JSON body
    4. Build update dict with only provided fields
    5. Update menu_items table: UPDATE ... WHERE id = :item_id
    6. Return updated item

    Response: { "item": {...} }
    """
    pass


def delete_menu_item(item_id):
    """
    DELETE /api/admin/menu/items/<item_id>

    Delete a menu item.

    Headers: Authorization (admin only)
    URL Params: item_id (int)

    Steps:
    1. Use @require_admin decorator
    2. Get item by ID — verify it exists
    3. Delete from menu_items table: DELETE FROM menu_items WHERE id = :item_id
    4. Return success message

    Response: { "message": "Item deleted" }
    """
    pass


# ──────────────────────────────────────────────
# Stats / Analytics
# ──────────────────────────────────────────────


def get_stats():
    """
    GET /api/admin/stats

    Get dashboard statistics.

    Headers: Authorization (admin only)

    Steps:
    1. Use @require_admin decorator
    2. Query today's order count:
       SELECT COUNT(*) FROM orders WHERE DATE(created_at) = CURRENT_DATE
    3. Query pending order count:
       SELECT COUNT(*) FROM orders WHERE status = 'pending'
    4. Query today's revenue:
       SELECT COALESCE(SUM(total_amount), 0) FROM orders
       WHERE DATE(created_at) = CURRENT_DATE AND status IN ('approved', 'ready', 'completed')
    5. Query popular items (top 5):
       SELECT mi.name, SUM(oi.quantity) as count
       FROM order_items oi
       JOIN menu_items mi ON oi.menu_item_id = mi.id
       JOIN orders o ON oi.order_id = o.id
       WHERE DATE(o.created_at) = CURRENT_DATE
       GROUP BY mi.name
       ORDER BY count DESC LIMIT 5
    6. Return stats object

    Response: { "today_orders": 45, "pending_orders": 3, "today_revenue": 2500, "popular_items": [...] }
    """
    pass
