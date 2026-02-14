# Database Schema

## Overview

The database is hosted on **Supabase** (managed PostgreSQL). No local database setup needed.

Supabase provides:

- **Auth** — manages `auth.users` table automatically
- **Database** — our custom tables in the `public` schema
- **Storage** — file storage for menu item images (bucket: `menu-images`)

---

## Tables

### 1. `users`

Extends Supabase's `auth.users` with profile data.

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    telegram_id BIGINT UNIQUE,
    role VARCHAR(20) DEFAULT 'student' CHECK (role IN ('student', 'admin')),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

| Column      | Type         | Notes                                |
| ----------- | ------------ | ------------------------------------ |
| id          | UUID         | FK to auth.users, primary key        |
| name        | VARCHAR(255) | Required                             |
| email       | VARCHAR(255) | Unique                               |
| phone       | VARCHAR(20)  | Optional                             |
| telegram_id | BIGINT       | Optional, unique — for notifications |
| role        | VARCHAR(20)  | 'student' or 'admin'                 |
| created_at  | TIMESTAMP    | Auto-set                             |
| updated_at  | TIMESTAMP    | Auto-set                             |

### 2. `food_stalls`

```sql
CREATE TABLE food_stalls (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    image_url VARCHAR(500),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

| Column      | Type         | Notes              |
| ----------- | ------------ | ------------------ |
| id          | SERIAL       | Auto-increment     |
| name        | VARCHAR(255) | Required           |
| description | TEXT         | Optional           |
| image_url   | VARCHAR(500) | URL to stall image |
| is_active   | BOOLEAN      | Show/hide stall    |
| created_at  | TIMESTAMP    | Auto-set           |
| updated_at  | TIMESTAMP    | Auto-set           |

### 3. `menu_items`

```sql
CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    stall_id INTEGER NOT NULL REFERENCES food_stalls(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    image_url VARCHAR(500),
    category VARCHAR(50) NOT NULL CHECK (category IN ('main', 'snack', 'beverage', 'dessert')),
    is_available BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

| Column       | Type          | Notes                                     |
| ------------ | ------------- | ----------------------------------------- |
| id           | SERIAL        | Auto-increment                            |
| stall_id     | INTEGER       | FK to food_stalls                         |
| name         | VARCHAR(255)  | Required                                  |
| description  | TEXT          | Optional                                  |
| price        | DECIMAL(10,2) | Must be >= 0                              |
| image_url    | VARCHAR(500)  | URL from Supabase Storage                 |
| category     | VARCHAR(50)   | 'main', 'snack', 'beverage', or 'dessert' |
| is_available | BOOLEAN       | Toggle item availability                  |
| created_at   | TIMESTAMP     | Auto-set                                  |
| updated_at   | TIMESTAMP     | Auto-set                                  |

### 4. `orders`

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    stall_id INTEGER NOT NULL REFERENCES food_stalls(id),
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'ready', 'completed')),
    rejection_reason TEXT,
    estimated_time INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

| Column           | Type          | Notes                                             |
| ---------------- | ------------- | ------------------------------------------------- |
| id               | SERIAL        | Auto-increment                                    |
| user_id          | UUID          | FK to users                                       |
| stall_id         | INTEGER       | FK to food_stalls                                 |
| total_amount     | DECIMAL(10,2) | Sum of all items                                  |
| status           | VARCHAR(20)   | pending → approved → ready → completed / rejected |
| rejection_reason | TEXT          | Set when admin rejects                            |
| estimated_time   | INTEGER       | Minutes until ready (set on approve)              |
| created_at       | TIMESTAMP     | Auto-set                                          |
| updated_at       | TIMESTAMP     | Auto-set                                          |

### 5. `order_items`

```sql
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INTEGER NOT NULL REFERENCES menu_items(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price_at_order DECIMAL(10, 2) NOT NULL CHECK (price_at_order >= 0),
    created_at TIMESTAMP DEFAULT NOW()
);
```

| Column         | Type          | Notes                        |
| -------------- | ------------- | ---------------------------- |
| id             | SERIAL        | Auto-increment               |
| order_id       | INTEGER       | FK to orders                 |
| menu_item_id   | INTEGER       | FK to menu_items             |
| quantity       | INTEGER       | Must be > 0                  |
| price_at_order | DECIMAL(10,2) | Price snapshot at order time |
| created_at     | TIMESTAMP     | Auto-set                     |

---

## Indexes

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created_at ON orders(created_at);
CREATE INDEX idx_menu_items_stall_id ON menu_items(stall_id);
CREATE INDEX idx_menu_items_category ON menu_items(category);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

---

## Seed Data

### Food Stalls

```sql
INSERT INTO food_stalls (name, description, is_active) VALUES
('South Indian Corner', 'Authentic South Indian breakfast and snacks', true),
('Juice & Snacks Bar', 'Fresh juices, sandwiches, and quick bites', true),
('North Indian Dhaba', 'Roti, sabzi, dal, and rice meals', true);
```

### Menu Items

```sql
INSERT INTO menu_items (stall_id, name, description, price, category, is_available) VALUES
(1, 'Masala Dosa', 'Crispy dosa with potato filling', 40.00, 'main', true),
(1, 'Idli (2 pcs)', 'Steamed rice cakes with sambar and chutney', 20.00, 'main', true),
(1, 'Vada (2 pcs)', 'Deep fried lentil donuts', 25.00, 'snack', true),
(1, 'Filter Coffee', 'Traditional South Indian filter coffee', 15.00, 'beverage', true),
(2, 'Mango Juice', 'Fresh mango juice', 30.00, 'beverage', true),
(2, 'Veg Sandwich', 'Grilled vegetable sandwich', 35.00, 'snack', true),
(2, 'Samosa (2 pcs)', 'Crispy potato samosas', 20.00, 'snack', true),
(3, 'Roti Sabzi', '3 rotis with seasonal vegetable curry', 50.00, 'main', true),
(3, 'Dal Rice', 'Dal tadka with steamed rice', 45.00, 'main', true),
(3, 'Curd Rice', 'Yogurt rice with tempering', 30.00, 'main', true);
```

### Admin User

```sql
-- Create admin through Supabase Auth first (register via dashboard or API)
-- Then update the role in the users table:
-- UPDATE users SET role = 'admin' WHERE email = 'admin@lbrce.edu.in';
```

---

## Supabase Storage

Create a **public** storage bucket called `menu-images` for dish photos.

```
Supabase Dashboard → Storage → New Bucket
  Name: menu-images
  Public: Yes (so image URLs are accessible without auth)
```

Images are uploaded directly from the frontend using the Supabase JS client. The API only stores the resulting public URL string.

---

## Entity Relationship Diagram

```
auth.users (managed by Supabase)
    │
    │ 1:1
    ▼
┌────────────┐
│   users     │
│ (profiles)  │
└─────┬──────┘
      │ 1:N
      ▼
┌────────────┐       ┌──────────────┐
│   orders    │──────▶│ food_stalls   │
└─────┬──────┘  N:1  └──────┬───────┘
      │ 1:N                  │ 1:N
      ▼                      ▼
┌──────────────┐      ┌──────────────┐
│ order_items   │─────▶│ menu_items    │
└──────────────┘  N:1 └──────────────┘
```
