"""
Menu Routes
===========
Blueprint: menu_bp
Prefix: /api/menu

Endpoints:
    GET /menu/stalls                  — List all active food stalls
    GET /menu/stalls/<stall_id>/items — List menu items for a stall
    GET /menu/items/<item_id>         — Get a single menu item
    GET /menu/search                  — Search menu items by name

These endpoints are PUBLIC — no auth required.
"""

# from flask import Blueprint, request, jsonify
# from services.supabase_service import get_supabase_client

# menu_bp = Blueprint("menu", __name__)


def get_stalls():
    """
    GET /menu/stalls

    Steps:
    1. Query food_stalls table: SELECT * FROM food_stalls WHERE is_active = true
    2. Return list of stalls with 200 status
    """
    pass


def get_stall_items():
    """
    GET /menu/stalls/<stall_id>/items
    Query params: ?category=main (optional)

    Steps:
    1. Get stall_id from URL path
    2. Get optional category from query params
    3. Query menu_items table:
       SELECT * FROM menu_items WHERE stall_id = <stall_id> AND is_available = true
    4. If category param provided, add: AND category = <category>
    5. Return list of menu items with 200 status
    """
    pass


def get_item():
    """
    GET /menu/items/<item_id>

    Steps:
    1. Get item_id from URL path
    2. Query menu_items table: SELECT * FROM menu_items WHERE id = <item_id>
    3. If not found, return 404
    4. Return menu item with 200 status
    """
    pass


def search_items():
    """
    GET /menu/search?q=dosa

    Steps:
    1. Get search query 'q' from query params
    2. If q is empty, return 400
    3. Query menu_items table with ILIKE:
       SELECT mi.*, fs.name as stall_name
       FROM menu_items mi
       JOIN food_stalls fs ON mi.stall_id = fs.id
       WHERE mi.name ILIKE '%<q>%' AND mi.is_available = true
    4. Return matching items with 200 status
    """
    pass
