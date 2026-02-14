"""
Main Flask Application
======================
Entry point for the Campus Food Court API.

This file:
1. Creates the Flask app instance
2. Loads configuration from config.py
3. Enables CORS for frontend (GitHub Pages) requests
4. Registers all route blueprints (auth, users, menu, orders, admin)
5. Defines a health-check route at GET /
6. Runs the app on the configured port
"""

# ──────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────
# from flask import Flask, jsonify
# from flask_cors import CORS
# from config import Config
# from routes.auth import auth_bp
# from routes.users import users_bp
# from routes.menu import menu_bp
# from routes.orders import orders_bp
# from routes.admin import admin_bp


def create_app():
    """
    Application factory.

    Steps:
    1. Create Flask instance
    2. Load config from Config class
    3. Enable CORS — allow requests from GitHub Pages domain and localhost
       - CORS(app, resources={r"/api/*": {"origins": ["http://localhost:*", "https://<user>.github.io"]}})
    4. Register blueprints with /api prefix:
       - auth_bp   → /api/auth
       - users_bp  → /api/users
       - menu_bp   → /api/menu
       - orders_bp → /api/orders
       - admin_bp  → /api/admin
    5. Define GET / route that returns {"status": "ok", "message": "LBRCE Food Court API"}
    6. Return app instance
    """
    pass


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────
# if __name__ == "__main__":
#     app = create_app()
#     port = app.config.get("FLASK_PORT", 5000)
#     debug = app.config.get("FLASK_ENV") == "development"
#     app.run(host="0.0.0.0", port=port, debug=debug)
