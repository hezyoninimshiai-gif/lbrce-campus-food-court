# ──────────────────────────────────────────────
# Stage 1: Python base image
# ──────────────────────────────────────────────
FROM python:3.12-slim

# ──────────────────────────────────────────────
# Set working directory inside the container
# ──────────────────────────────────────────────
WORKDIR /app

# ──────────────────────────────────────────────
# Copy requirements first (for Docker layer caching)
# If requirements.txt hasn't changed, pip install
# is skipped on rebuild — saves time
# ──────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ──────────────────────────────────────────────
# Copy the rest of the application code
# ──────────────────────────────────────────────
COPY . .

# ──────────────────────────────────────────────
# Expose port 5000 (Flask default)
# ──────────────────────────────────────────────
EXPOSE 5000

# ──────────────────────────────────────────────
# Run with gunicorn in production
# - Binds to 0.0.0.0:5000
# - 2 worker processes (lightweight server)
# - app:create_app() is the Flask factory
# ──────────────────────────────────────────────
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
