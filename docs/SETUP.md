# Setup Instructions

## Prerequisites (All Teams)

- Git installed
- GitHub account
- Code editor (VS Code recommended)

---

## Team 1: Database + Infrastructure

### Supabase Setup

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project — note down:
   - **Project URL** (e.g., `https://xyzcompany.supabase.co`)
   - **anon public key** (found in Settings → API)
   - **service_role key** (found in Settings → API — keep this secret!)
3. Go to **SQL Editor** in the Supabase dashboard
4. Copy the schema from `docs/DB_SCHEMA.md` and run it
5. Run the seed data SQL statements from the same file
6. Go to **Storage** → Create a new bucket:
   - Name: `menu-images`
   - Public: **Yes**
7. Share the Supabase URL and anon key with Team 2 (backend) and Team 4 (frontend)
8. Share the service_role key with Team 2 ONLY (never expose in frontend)

### Ubuntu Server Setup

1. Get access to a local Ubuntu server (or a VM)
2. Note down the server's IP address
3. Setup SSH access (password or key-based)
4. Run: `sudo apt update && sudo apt install -y docker.io`
5. Add your user to the docker group: `sudo usermod -aG docker $USER`
6. Log out and back in for group changes to take effect
7. Verify: `docker --version`
8. Share the server IP and SSH credentials with Team 5

---

## Team 2: Backend API

### Local Development

1. Install Python 3.10+ — verify with `python3 --version`
2. Navigate to the `api/` folder
3. Create a virtual environment:
   ```bash
   cd api
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   # venv\Scripts\activate     # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and fill in values:
   ```bash
   cp .env.example .env
   ```
   Fill in:
   - `SUPABASE_URL` — from Team 1
   - `SUPABASE_KEY` — the **service_role** key from Team 1
   - `TELEGRAM_BOT_TOKEN` — from Team 3
6. Run the Flask app:
   ```bash
   python app.py
   ```
   API will be at `http://localhost:5000`

### Testing Endpoints

Use a REST client (Postman, Insomnia, or `curl`):

```bash
# Test health check
curl http://localhost:5000/api/menu/stalls

# Test with auth
curl -H "Authorization: Bearer <token>" http://localhost:5000/api/users/profile
```

---

## Team 3: Telegram Notifications

### Create Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow prompts to name your bot (e.g., "LBRCE Food Court Bot")
4. Copy the **bot token** — share with Team 2 for the `.env` file
5. To get your own chat ID for testing:
   - Send a message to your bot
   - Visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
   - Find `chat.id` in the response

### Development

1. Work in `api/services/telegram.py`
2. The function is simple — just `requests.post()` to Telegram API
3. Test by running the Flask app and triggering an order status change

### How Users Link Telegram

1. User opens the bot in Telegram and sends `/start`
2. Bot responds with their chat ID (or user finds it via the getUpdates API)
3. User enters this chat ID in their profile page on the website
4. The API stores the `telegram_id` in the `users` table
5. When order status changes, the API looks up the user's `telegram_id` and sends a message

---

## Team 4: Frontend

### Local Development

No build tools needed! Just open HTML files in a browser.

1. Navigate to the `frontend/` folder
2. Open `index.html` in a browser — or use VS Code Live Server extension:
   - Install "Live Server" extension in VS Code
   - Right-click `index.html` → "Open with Live Server"
3. Update `js/config.js` with:
   - `SUPABASE_URL` — from Team 1
   - `SUPABASE_ANON_KEY` — the **anon public** key from Team 1 (safe for frontend)
   - `API_URL` — `http://localhost:5000/api` for local dev

### Image Upload (Admin Menu Management)

1. When admin adds/edits a menu item, they select an image file
2. Frontend uploads the image to Supabase Storage bucket `menu-images`
3. Uses the Supabase JS client (loaded via CDN):
   ```javascript
   const { data, error } = await supabase.storage
     .from("menu-images")
     .upload(`${Date.now()}-${file.name}`, file);
   ```
4. Get the public URL:
   ```javascript
   const { data: urlData } = supabase.storage
     .from("menu-images")
     .getPublicUrl(data.path);
   ```
5. Send the URL as `image_url` in the API request

### Structure

- Each HTML page is standalone with its own JS file
- Shared logic lives in `js/auth.js`, `js/api.js`, `js/supabase.js`
- Cart uses `localStorage` — no backend needed for cart storage
- Bootstrap handles responsive design — use Bootstrap classes
- All CDN links are already in the HTML `<head>` sections

---

## Team 5: CI/CD + Deployment

### GitHub Actions

1. The workflow file is at `.github/workflows/api-ci.yml`
2. It runs automatically on push to `main` branch
3. It builds the API Docker image to verify the build works
4. No deployment step in CI — deployment is done manually via Ansible

### GitHub Pages

1. Go to the repo on GitHub → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/frontend`
4. Save — GitHub will publish the frontend at `https://<username>.github.io/lbrce-campus-food-court/`
5. No CI/CD needed — GitHub Pages auto-deploys on push

### Ansible

1. Install Ansible on your local machine:

   ```bash
   # macOS
   brew install ansible

   # Ubuntu
   sudo apt install ansible
   ```

2. Update `ansible/hosts.ini` with the server IP and SSH details from Team 1
3. Run setup (first time only):
   ```bash
   cd ansible
   ansible-playbook -i hosts.ini setup.yml
   ```
4. Deploy the API:
   ```bash
   cd ansible
   ansible-playbook -i hosts.ini deploy.yml
   ```

---

## Environment Variables Reference

| Variable           | Used By  | Where to Get                             |
| ------------------ | -------- | ---------------------------------------- |
| SUPABASE_URL       | API + FE | Supabase Dashboard → Settings            |
| SUPABASE_KEY       | API      | Supabase → Settings → API → service_role |
| SUPABASE_ANON_KEY  | FE       | Supabase → Settings → API → anon         |
| TELEGRAM_BOT_TOKEN | API      | BotFather on Telegram                    |
| FLASK_ENV          | API      | Set to `development` locally             |
| FLASK_PORT         | API      | Default: 5000                            |
