# API — Campus Food Court Backend

## Overview

Flask REST API that connects to Supabase (PostgreSQL + Auth) and sends Telegram notifications.

## Team 2 Responsibilities

- Implement all route handlers in `routes/`
- Implement services in `services/`
- Implement auth middleware in `middleware/`
- All code files currently have **comments only** — your job is to implement them

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy env file and fill in values
cp .env.example .env

# Run the app
python app.py
```

API will be available at `http://localhost:5000`

## Project Structure

```
api/
├── app.py                  # Flask app factory, registers blueprints
├── config.py               # Loads env vars
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── Dockerfile              # Container build file
├── routes/
│   ├── __init__.py
│   ├── auth.py             # POST /auth/register, /auth/login, /auth/logout
│   ├── users.py            # GET/PUT /users/profile
│   ├── menu.py             # GET /menu/stalls, /menu/stalls/:id/items, /menu/items/:id, /menu/search
│   ├── orders.py           # POST /orders, GET /orders, GET /orders/:id
│   └── admin.py            # Admin order management + menu management + stats
├── services/
│   ├── __init__.py
│   ├── supabase_service.py # Supabase client wrapper
│   ├── order_service.py    # Order business logic
│   └── telegram.py         # Telegram notification functions
└── middleware/
    ├── __init__.py
    └── auth_middleware.py   # @require_auth and @require_admin decorators
```

## Environment Variables

| Variable           | Description                       |
| ------------------ | --------------------------------- |
| SUPABASE_URL       | Supabase project URL              |
| SUPABASE_KEY       | Supabase service_role key         |
| TELEGRAM_BOT_TOKEN | Telegram bot token from BotFather |
| FLASK_ENV          | development or production         |
| FLASK_PORT         | Port number (default: 5000)       |

## Key Integration Points

- **Team 1**: Provides Supabase URL and keys, sets up the database schema
- **Team 3**: Implements `services/telegram.py` notification functions
- **Team 4**: Frontend calls these API endpoints via `fetch()`
- **Team 5**: Builds and runs this as a Docker container

## API Docs

See `docs/API_SPEC.md` for the complete endpoint specification.
