# Frontend — Campus Food Court

## Overview

Static HTML pages with Bootstrap 5 (CDN) and vanilla JavaScript. Hosted on GitHub Pages.

## Team 4 Responsibilities

- Build all HTML pages with Bootstrap components
- Implement JavaScript logic for each page
- Integrate with Supabase Auth (login/register)
- Integrate with backend API (fetch calls)
- Upload menu images to Supabase Storage
- Make everything mobile-first (responsive)
- All JS files currently have **comments only** — your job is to implement them

## Setup

No build tools needed. Just open HTML files in a browser.

**Recommended:** Use VS Code with the "Live Server" extension for auto-reload during development.

1. Right-click `index.html` → "Open with Live Server"
2. Update `js/config.js` with your Supabase URL and anon key

## Configuration

Edit `js/config.js`:

```javascript
const SUPABASE_URL = "https://your-project.supabase.co";
const SUPABASE_ANON_KEY = "your-anon-public-key";
const API_URL = "http://localhost:5000/api";
const STORAGE_BUCKET = "menu-images";
```

## Pages

| File            | Purpose                             | Auth Required  |
| --------------- | ----------------------------------- | -------------- |
| index.html      | Landing page, browse food stalls    | No             |
| login.html      | Login and register forms            | No             |
| menu.html       | View menu items for a stall         | No             |
| cart.html       | Shopping cart, place order          | Yes (to order) |
| orders.html     | Order history and status tracking   | Yes            |
| profile.html    | User profile, link Telegram ID      | Yes            |
| admin.html      | Admin dashboard, manage orders      | Yes (admin)    |
| admin-menu.html | Admin menu management, image upload | Yes (admin)    |

## JavaScript Files

| File          | Purpose                                         |
| ------------- | ----------------------------------------------- |
| config.js     | Supabase URL, API URL, storage bucket constants |
| supabase.js   | Initialize Supabase client from CDN             |
| auth.js       | Login, register, logout, auth guards            |
| api.js        | Fetch wrapper for backend API calls             |
| home.js       | index.html — load and display stalls            |
| menu.js       | menu.html — display items, category filter      |
| cart.js       | Cart management (localStorage) + place order    |
| orders.js     | orders.html — order history, status filter      |
| profile.js    | profile.html — view/update profile              |
| admin.js      | admin.html — stats, pending orders, actions     |
| admin-menu.js | admin-menu.html — CRUD menu items, image upload |

## Deployment

GitHub Pages — no build step needed:

1. Go to repo Settings → Pages
2. Source: Deploy from branch
3. Branch: `main`, Folder: `/frontend`
4. Save

## Key Integration Points

- **Team 1**: Provides Supabase URL and anon key for `config.js`
- **Team 2**: Provides the API endpoints this frontend calls
- **Team 3**: Users link their Telegram ID via the profile page
- **Team 5**: Enables GitHub Pages in repo settings
