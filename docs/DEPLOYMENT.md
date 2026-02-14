# Deployment Guide

## Architecture

```
┌──────────────────────────────┐
│  GitHub Pages                │
│  (Static HTML/CSS/JS)        │
│  https://<user>.github.io/   │
│  lbrce-campus-food-court/    │
└──────────┬───────────────────┘
           │ API calls (fetch)
           ▼
┌──────────────────────────────┐
│  Ubuntu Server               │
│  Docker Container            │
│  Flask API on port 5000      │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Supabase (Cloud)            │
│  PostgreSQL + Auth + Storage │
└──────────────────────────────┘
```

---

## 1. Frontend Deployment (GitHub Pages)

GitHub Pages serves the static frontend files directly from the repository.

### Steps

1. Push all frontend code to the `main` branch
2. Go to **GitHub repo → Settings → Pages**
3. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: `/frontend`
4. Click **Save**
5. Wait 1-2 minutes — your site will be live at:
   ```
   https://<your-username>.github.io/lbrce-campus-food-court/
   ```

### Update Frontend Config for Production

Before deploying, update `frontend/js/config.js`:

```javascript
const API_URL = "http://<your-server-ip>:5000/api";
const SUPABASE_URL = "https://<your-project>.supabase.co";
const SUPABASE_ANON_KEY = "<your-anon-key>";
```

### Notes

- No build step needed — files are served as-is
- Updates auto-deploy when you push to `main`
- No CI workflow needed for frontend

---

## 2. Backend Deployment (Docker on Ubuntu)

The Flask API runs as a single Docker container on an Ubuntu server.

### Manual Deployment

SSH into the server and run:

```bash
# Clone the repository (first time)
git clone https://github.com/<your-org>/lbrce-campus-food-court.git
cd lbrce-campus-food-court

# Create .env file with production values
cat > api/.env << 'EOF'
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=<your-service-role-key>
TELEGRAM_BOT_TOKEN=<your-bot-token>
FLASK_ENV=production
FLASK_PORT=5000
EOF

# Build the Docker image
docker build -t lbrce-api ./api

# Stop old container (if running)
docker stop lbrce-api-container 2>/dev/null
docker rm lbrce-api-container 2>/dev/null

# Run the container
docker run -d \
  --name lbrce-api-container \
  -p 5000:5000 \
  --env-file api/.env \
  --restart unless-stopped \
  lbrce-api
```

### Update Deployment

```bash
cd lbrce-campus-food-court
git pull origin main

docker build -t lbrce-api ./api
docker stop lbrce-api-container
docker rm lbrce-api-container
docker run -d \
  --name lbrce-api-container \
  -p 5000:5000 \
  --env-file api/.env \
  --restart unless-stopped \
  lbrce-api
```

### Verify

```bash
# Check container is running
docker ps

# Check logs
docker logs lbrce-api-container

# Test endpoint
curl http://localhost:5000/api/menu/stalls
```

---

## 3. Automated Deployment with Ansible

### Prerequisites

- Ansible installed on your local machine
- SSH access to the Ubuntu server
- Server IP and credentials

### First-Time Server Setup

```bash
cd ansible
ansible-playbook -i hosts.ini setup.yml
```

This installs Docker on the server.

### Deploy / Update

```bash
cd ansible
ansible-playbook -i hosts.ini deploy.yml
```

This will:

1. Clone/pull the latest code on the server
2. Build the Docker image
3. Stop the old container
4. Start a new container with updated code

---

## 4. Supabase (No Deployment Needed)

Supabase is a managed cloud service. No deployment steps needed.

Ensure:

- Schema and seed data are loaded (Team 1)
- Storage bucket `menu-images` is created with public access
- Row Level Security (RLS) policies are configured if needed
- API keys are correct in both backend `.env` and frontend `config.js`

---

## Environment Checklist

Before going live, verify:

- [ ] Supabase project is set up with schema and seed data
- [ ] Supabase Storage bucket `menu-images` exists (public)
- [ ] Frontend `config.js` has production API URL and Supabase keys
- [ ] Backend `.env` has production Supabase URL, service_role key, and Telegram token
- [ ] Docker container is running on the server
- [ ] Frontend is accessible via GitHub Pages URL
- [ ] API is accessible at `http://<server-ip>:5000/api/menu/stalls`
- [ ] CORS is configured in Flask to allow requests from GitHub Pages domain
- [ ] Telegram bot is created and token is set

---

## Troubleshooting

### API container won't start

```bash
docker logs lbrce-api-container
```

Common issues:

- Missing `.env` file or variables
- Port 5000 already in use: `sudo lsof -i :5000`

### Frontend can't reach API

- Check CORS settings in Flask — must allow the GitHub Pages domain
- Verify API URL in `frontend/js/config.js`
- Check if the server firewall allows port 5000

### Telegram notifications not working

- Verify bot token is correct
- Ensure user has a `telegram_id` set in their profile
- Test manually: `curl "https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<ID>&text=test"`

### GitHub Pages not updating

- Check that you pushed to `main` branch
- Verify Pages is configured to deploy from `main` / `/frontend`
- Wait 2-3 minutes — GitHub Pages can be slow to update
