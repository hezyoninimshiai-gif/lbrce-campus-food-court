"""
User Routes
===========
Blueprint: users_bp
Prefix: /api/users

Endpoints:
    GET  /users/profile  — Get current user's profile
    PUT  /users/profile  — Update current user's profile

Both endpoints require Authorization header (JWT).
"""

# from flask import Blueprint, request, jsonify
# from services.supabase_service import get_supabase_client
# from middleware.auth_middleware import require_auth

# users_bp = Blueprint("users", __name__)


def get_profile():
    """
    GET /users/profile
    Headers: Authorization: Bearer <token>

    Steps:
    1. Extract user_id from the verified JWT (set by auth middleware)
    2. Query the `users` table: SELECT * FROM users WHERE id = user_id
    3. If user not found, return 404
    4. Return user profile data (id, name, email, phone, telegram_id, role)
    """
    pass


def update_profile():
    """
    PUT /users/profile
    Headers: Authorization: Bearer <token>

    Request Body (all fields optional):
        {
            "name": "Ramesh K",
            "phone": "9876543210",
            "telegram_id": "123456789"
        }

    Steps:
    1. Extract user_id from the verified JWT
    2. Parse JSON body — get name, phone, telegram_id (all optional)
    3. Build update dict with only provided fields
    4. Update the `users` table: UPDATE users SET ... WHERE id = user_id
    5. Return updated user profile with 200 status
    """
    pass
