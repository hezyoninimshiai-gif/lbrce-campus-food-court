# Task Tracker — LBRCE Campus Food Court

## Team 1: Database + Infrastructure

- [ ] Create Supabase account and project
- [ ] Run schema.sql in Supabase SQL editor
- [ ] Create Supabase Storage bucket `menu-images` with public access
- [ ] Run seed data
- [ ] Setup local Ubuntu server with Docker installed
- [ ] Create Ansible inventory file with server IP
- [ ] Document Supabase credentials location (URL, anon key, service role key)

## Team 2: Backend API

- [ ] Setup Flask project structure
- [ ] Configure Supabase client in `services/supabase_service.py`
- [ ] Implement auth endpoints (register, login, logout)
- [ ] Implement user profile endpoints (get, update with telegram_id)
- [ ] Implement menu endpoints (stalls, items by stall, item detail, search)
- [ ] Implement order creation endpoint
- [ ] Implement order listing endpoint (with status filter)
- [ ] Implement order detail endpoint
- [ ] Implement admin order management (approve, reject, ready, complete)
- [ ] Implement admin menu management (add, edit, delete items)
- [ ] Implement admin stats endpoint
- [ ] Implement auth middleware (JWT verification, admin role check)
- [ ] Add CORS support for GitHub Pages frontend
- [ ] Create Dockerfile for API
- [ ] Document all API endpoints

## Team 3: Telegram Notifications

- [ ] Create bot with BotFather on Telegram, get bot token
- [ ] Write `api/services/telegram.py` — `send_message(chat_id, text)` function
- [ ] Implement order approved notification template
- [ ] Implement order rejected notification template
- [ ] Implement order ready notification template
- [ ] Implement new order notification for admin
- [ ] Test notification delivery (send test message to your own Telegram)
- [ ] Document how students/admins find their Telegram chat ID
- [ ] Document how to link Telegram chat ID in user profile

## Team 4: Frontend

- [ ] Create base HTML layout with Bootstrap CDN navbar + footer
- [ ] Build login/register page (`login.html`)
- [ ] Integrate Supabase Auth (login, register, logout, session persistence)
- [ ] Build stalls browsing page (`index.html`)
- [ ] Build menu items page with dish images (`menu.html`)
- [ ] Build shopping cart with localStorage (`cart.html`)
- [ ] Build order placement flow (cart → API call → confirmation)
- [ ] Build order history page (`orders.html`)
- [ ] Build user profile page with Telegram ID field (`profile.html`)
- [ ] Build admin dashboard with pending orders and stats (`admin.html`)
- [ ] Build admin menu management with image upload (`admin-menu.html`)
- [ ] Implement image upload to Supabase Storage in admin menu page
- [ ] Auth guards — redirect to login if not authenticated
- [ ] Admin guards — redirect if user is not admin
- [ ] Make all pages responsive (mobile-first)
- [ ] Configure GitHub Pages to serve from `frontend/` folder

## Team 5: CI/CD + Deployment

- [ ] Create GitHub Actions workflow for API Docker build (`api-ci.yml`)
- [ ] Enable GitHub Pages for frontend (repo settings → Pages → source: `frontend/` folder)
- [ ] Write Ansible playbook to install Docker on Ubuntu server (`setup.yml`)
- [ ] Write Ansible playbook to clone repo, build image, and run container (`deploy.yml`)
- [ ] Create `hosts.ini` with Ubuntu server details
- [ ] Test end-to-end deployment (API accessible, frontend loads, orders work)
