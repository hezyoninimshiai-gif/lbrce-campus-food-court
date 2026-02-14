"""
Order Service
=============
Business logic for order operations.

Separated from routes to keep route handlers thin.
Routes parse requests and return responses; this module
handles the database operations and calculations.
"""

# from services.supabase_service import get_supabase_client
# from services.telegram import notify_admin_new_order


def create_new_order(user_id, stall_id, items):
    """
    Create a new order with all its items.

    Args:
        user_id (str): UUID of the user placing the order
        stall_id (int): ID of the food stall
        items (list): List of dicts: [{"menu_item_id": int, "quantity": int}, ...]

    Steps:
    1. Get Supabase client
    2. Fetch menu items from database for all menu_item_ids in the items list
    3. Validate:
       a. All menu_item_ids exist
       b. All items belong to the specified stall_id
       c. All items are available (is_available = true)
    4. Calculate total_amount:
       total = sum(item_price * quantity for each item)
    5. Insert into orders table:
       { user_id, stall_id, total_amount, status: 'pending' }
    6. Get the new order_id from the insert response
    7. For each item, insert into order_items table:
       { order_id, menu_item_id, quantity, price_at_order: item_price }
    8. Call notify_admin_new_order(order_id, user_id, stall_id, total_amount)
    9. Return order details dict

    Returns:
        dict: { "order_id": int, "total_amount": float, "status": "pending", "created_at": str }

    Raises:
        ValueError: If validation fails (invalid item, unavailable, wrong stall)
    """
    pass


def get_user_orders(user_id, status_filter=None):
    """
    Get all orders for a specific user.

    Args:
        user_id (str): UUID of the user
        status_filter (str, optional): Filter by status ('pending', 'approved', etc.)

    Steps:
    1. Get Supabase client
    2. Query orders table:
       - SELECT * FROM orders WHERE user_id = :user_id
       - If status_filter provided: AND status = :status_filter
       - ORDER BY created_at DESC
    3. For each order, fetch order_items with menu_item details:
       - SELECT oi.*, mi.name, mi.image_url
         FROM order_items oi
         JOIN menu_items mi ON oi.menu_item_id = mi.id
         WHERE oi.order_id = :order_id
    4. For each order, fetch stall name from food_stalls table
    5. Assemble complete order objects with nested items and stall info

    Returns:
        list: List of order dicts with items and stall data
    """
    pass


def get_order_detail(order_id, user_id):
    """
    Get detailed info for a single order (must belong to the user).

    Args:
        order_id (int): ID of the order
        user_id (str): UUID of the authenticated user

    Steps:
    1. Get Supabase client
    2. Query orders table: WHERE id = :order_id AND user_id = :user_id
    3. If not found, return None (route handler will return 404)
    4. Fetch order_items with menu_item details
    5. Fetch stall info
    6. Return complete order dict

    Returns:
        dict or None: Order details or None if not found
    """
    pass
