"""
Order Routes
============
Blueprint: orders_bp
Prefix: /api/orders

Endpoints:
    POST /orders             — Place a new order
    GET  /orders             — List current user's orders
    GET  /orders/<order_id>  — Get details of a specific order

All endpoints require Authorization header (JWT).
"""

# from flask import Blueprint, request, jsonify
# from services.supabase_service import get_supabase_client
# from services.order_service import create_order, get_user_orders, get_order_detail
# from services.telegram import notify_admin_new_order
# from middleware.auth_middleware import require_auth

# orders_bp = Blueprint("orders", __name__)


def place_order():
    """
    POST /orders
    Headers: Authorization: Bearer <token>

    Request Body:
        {
            "stall_id": 1,
            "items": [
                { "menu_item_id": 1, "quantity": 2 },
                { "menu_item_id": 3, "quantity": 1 }
            ]
        }

    Steps:
    1. Extract user_id from verified JWT
    2. Parse JSON body — get stall_id, items list
    3. Validate: stall_id exists, all menu_item_ids exist and are available
    4. Calculate total_amount by summing (price * quantity) for each item
    5. Insert into orders table: (user_id, stall_id, total_amount, status='pending')
    6. Insert each item into order_items table: (order_id, menu_item_id, quantity, price_at_order)
    7. Call notify_admin_new_order() — sends Telegram message to admin if they have telegram_id
    8. Return order_id, total_amount, status, created_at with 201 status
    """
    pass


def list_orders():
    """
    GET /orders
    Headers: Authorization: Bearer <token>
    Query params: ?status=pending (optional)

    Steps:
    1. Extract user_id from verified JWT
    2. Get optional status filter from query params
    3. Query orders table:
       SELECT * FROM orders WHERE user_id = <user_id>
       If status param exists: AND status = <status>
       ORDER BY created_at DESC
    4. For each order, fetch order_items joined with menu_items
    5. For each order, fetch stall info
    6. Return list of orders with nested items and stall data
    """
    pass


def get_order():
    """
    GET /orders/<order_id>
    Headers: Authorization: Bearer <token>

    Steps:
    1. Extract user_id from verified JWT
    2. Get order_id from URL path
    3. Query orders table: SELECT * FROM orders WHERE id = <order_id> AND user_id = <user_id>
    4. If not found, return 404 (also prevents users from viewing others' orders)
    5. Fetch order_items joined with menu_items for this order
    6. Fetch stall info
    7. Return order details with nested items and stall data
    """
    pass
