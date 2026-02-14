"""
Auth Middleware
===============
Decorators for protecting Flask routes with JWT authentication.

Uses Supabase to verify JWT tokens from the Authorization header.
"""

# from functools import wraps
# from flask import request, jsonify
# from services.supabase_service import get_user_from_token, get_supabase_client


def require_auth(f):
    """
    Decorator: Require a valid JWT token.

    Usage:
        @app.route("/api/users/profile")
        @require_auth
        def get_profile():
            user_id = request.user_id  # set by this decorator
            ...

    Steps:
    1. Get the Authorization header from the request
    2. If missing, return 401 {"error": "Authorization header required"}
    3. Extract token: header.replace("Bearer ", "")
    4. Call get_user_from_token(token) to verify with Supabase
    5. If token is invalid/expired, return 401 {"error": "Invalid or expired token"}
    6. Set request.user_id = user.id (so the route handler can access it)
    7. Call the wrapped function f(*args, **kwargs)
    """
    pass


def require_admin(f):
    """
    Decorator: Require a valid JWT token AND admin role.

    Usage:
        @app.route("/api/admin/orders/pending")
        @require_admin
        def get_pending_orders():
            ...

    Steps:
    1. Do everything require_auth does (verify JWT, set user_id)
    2. Additionally, query the users table: SELECT role FROM users WHERE id = user_id
    3. If role != 'admin', return 403 {"error": "Admin access required"}
    4. Call the wrapped function

    Note: This decorator combines auth check + role check in one step.
    """
    pass
