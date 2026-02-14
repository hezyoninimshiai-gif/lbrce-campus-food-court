"""
Supabase Service
================
Wrapper around the Supabase Python client.

Provides a single shared Supabase client instance used by all
route handlers and services to query the database and auth.
"""

# from supabase import create_client, Client
# from config import Config


def get_supabase_client():
    """
    Create and return a Supabase client instance.

    Steps:
    1. Read SUPABASE_URL and SUPABASE_KEY from Config
    2. Call create_client(url, key) to create the client
    3. Return the client

    Usage:
        supabase = get_supabase_client()
        result = supabase.table("users").select("*").execute()

    Note: Consider caching the client instance (module-level variable)
    so we don't create a new client on every request.

    Returns:
        Client: Supabase client instance
    """
    pass


def get_user_from_token(token):
    """
    Verify a Supabase JWT token and return the user.

    Args:
        token (str): JWT access token from Authorization header

    Steps:
    1. Get Supabase client
    2. Call supabase.auth.get_user(token)
    3. If invalid token, raises an exception
    4. Return user object (contains id, email, etc.)

    Returns:
        dict: User data from Supabase Auth

    Raises:
        Exception: If token is invalid or expired
    """
    pass
