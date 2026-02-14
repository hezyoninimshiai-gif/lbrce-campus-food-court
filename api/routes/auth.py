"""
Auth Routes
===========
Blueprint: auth_bp
Prefix: /api/auth

Endpoints:
    POST /auth/register  — Register a new user
    POST /auth/login     — Login and get session token
    POST /auth/logout    — Logout (invalidate session)

All auth is handled by Supabase Auth. These routes act as a
thin proxy so the frontend has a consistent API base URL.
"""

# from flask import Blueprint, request, jsonify
# from services.supabase_service import get_supabase_client

# auth_bp = Blueprint("auth", __name__)


def register():
    """
    POST /auth/register

    Request Body:
        {
            "email": "student@lbrce.edu.in",
            "password": "mypassword",
            "name": "Ramesh Kumar",
            "phone": "9876543210"
        }

    Steps:
    1. Parse JSON body — get email, password, name, phone
    2. Call supabase.auth.sign_up({"email": email, "password": password})
    3. If sign_up fails, return error with 400 status
    4. Insert a row into the `users` table with id (from auth), name, email, phone
    5. Return user and session data with 201 status
    """
    pass


def login():
    """
    POST /auth/login

    Request Body:
        {
            "email": "student@lbrce.edu.in",
            "password": "mypassword"
        }

    Steps:
    1. Parse JSON body — get email, password
    2. Call supabase.auth.sign_in_with_password({"email": email, "password": password})
    3. If sign_in fails, return error with 401 status
    4. Return user and session data (includes access_token) with 200 status
    """
    pass


def logout():
    """
    POST /auth/logout
    Headers: Authorization: Bearer <token>

    Steps:
    1. Get the token from Authorization header
    2. Call supabase.auth.sign_out() or just acknowledge logout
    3. Return success message with 200 status

    Note: Supabase JWTs are stateless — "logout" is mostly client-side
    (clear token from localStorage). This endpoint exists for completeness.
    """
    pass
