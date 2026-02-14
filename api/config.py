"""
Configuration Management
========================
Loads environment variables and provides them to the Flask app.

Uses python-dotenv to read from .env file in development.
"""

# ──────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────
# import os
# from dotenv import load_dotenv
# load_dotenv()


class Config:
    """
    Application configuration loaded from environment variables.

    Attributes:
        SUPABASE_URL        (str): Supabase project URL (e.g., https://xyz.supabase.co)
        SUPABASE_KEY        (str): Supabase service_role key (secret — backend only)
        TELEGRAM_BOT_TOKEN  (str): Telegram bot token from BotFather
        FLASK_ENV           (str): 'development' or 'production'
        FLASK_PORT          (int): Port to run on (default 5000)

    Steps:
    1. Call load_dotenv() to read .env file
    2. Read each variable with os.environ.get() or os.getenv()
    3. Provide sensible defaults where appropriate
    4. Cast FLASK_PORT to int
    """

    pass
