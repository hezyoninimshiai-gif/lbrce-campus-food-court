# System Diagrams

> All diagrams use [Mermaid.js](https://mermaid.js.org/) syntax.
> You can preview them on GitHub (renders automatically), in VS Code with the **Mermaid Preview** extension, or at [mermaid.live](https://mermaid.live).

---

## 1. System Architecture

This shows **what** each piece of the system is and **how** they talk to each other.

```mermaid
graph TB
    subgraph "User Devices (Browser)"
        S["👨‍🎓 Student<br/>Opens website"]
        A["👩‍💼 Admin<br/>Opens website"]
    end

    subgraph "GitHub Pages (Free Hosting)"
        FE["📄 Frontend<br/>HTML + CSS + JS<br/>Bootstrap CDN"]
    end

    subgraph "Ubuntu Server (College/Cloud)"
        API["🐍 Flask API<br/>Running inside Docker<br/>Port 5000"]
    end

    subgraph "Supabase (Cloud - Free Tier)"
        AUTH["🔐 Supabase Auth<br/>Email + Password Login"]
        DB["🗄️ PostgreSQL Database<br/>Users, Orders, Menu, Stalls"]
        STORE["📦 Supabase Storage<br/>Bucket: menu-images<br/>Dish Photos"]
    end

    TEL["🤖 Telegram Bot API<br/>api.telegram.org<br/>Sends notifications"]
    PHONE["📱 Student's Telegram App"]

    %% User accesses frontend
    S -- "visits website" --> FE
    A -- "visits website" --> FE

    %% Frontend talks to services
    FE -- "login / register<br/>(Supabase JS SDK)" --> AUTH
    FE -- "upload dish image<br/>(Supabase JS SDK)" --> STORE
    FE -- "REST API calls<br/>(fetch with JWT token)" --> API

    %% API talks to Supabase
    API -- "read/write data<br/>(supabase-py)" --> DB
    API -- "verify JWT token" --> AUTH

    %% API sends Telegram messages
    API -- "requests.post()<br/>send notification" --> TEL
    TEL -- "message delivered" --> PHONE

    %% Styling
    style S fill:#e3f2fd,stroke:#1565c0,color:#000
    style A fill:#fff3e0,stroke:#e65100,color:#000
    style FE fill:#e8f5e9,stroke:#2e7d32,color:#000
    style API fill:#fce4ec,stroke:#c62828,color:#000
    style AUTH fill:#f3e5f5,stroke:#6a1b9a,color:#000
    style DB fill:#f3e5f5,stroke:#6a1b9a,color:#000
    style STORE fill:#f3e5f5,stroke:#6a1b9a,color:#000
    style TEL fill:#e0f7fa,stroke:#00695c,color:#000
    style PHONE fill:#e0f7fa,stroke:#00695c,color:#000
```

### Key Points for Students

| Component                      | Where it runs                     | Who builds it     |
| ------------------------------ | --------------------------------- | ----------------- |
| Frontend (HTML/CSS/JS)         | GitHub Pages (free)               | Team 4            |
| Flask API                      | Docker container on Ubuntu server | Team 2            |
| Supabase (DB + Auth + Storage) | Cloud (supabase.com, free tier)   | Team 1 sets it up |
| Telegram notifications         | Called from Flask API             | Team 3            |
| Docker + Ansible + CI          | Ubuntu server + GitHub Actions    | Team 5            |

---

## 2. How Login Works

What happens step-by-step when a student logs in.

```mermaid
sequenceDiagram
    actor Student
    participant Browser as Frontend (Browser)
    participant Supa as Supabase Auth
    participant API as Flask API
    participant DB as PostgreSQL (Supabase)

    Student->>Browser: Enters email & password, clicks "Login"

    Browser->>Supa: supabase.auth.signInWithPassword(email, password)
    Supa-->>Browser: ✅ Returns JWT token + user info

    Note over Browser: Browser stores JWT token<br/>in localStorage

    Browser->>API: GET /api/users/profile<br/>Header: Authorization: Bearer <JWT>
    API->>Supa: Verify JWT token is valid
    Supa-->>API: ✅ Token valid, user ID = abc123
    API->>DB: SELECT * FROM users WHERE id = 'abc123'
    DB-->>API: User record (name, email, phone, role)
    API-->>Browser: { name: "Ramesh", role: "student", ... }

    Note over Browser: Redirect to menu page
```

---

## 3. How Registration Works

What happens when a new student creates an account.

```mermaid
sequenceDiagram
    actor Student
    participant Browser as Frontend (Browser)
    participant Supa as Supabase Auth
    participant API as Flask API
    participant DB as PostgreSQL (Supabase)

    Student->>Browser: Fills name, email, password, phone

    Browser->>Supa: supabase.auth.signUp(email, password)
    Supa-->>Browser: ✅ New auth user created, returns JWT + user ID

    Browser->>API: POST /api/auth/register<br/>Body: { name, email, phone }<br/>Header: Authorization: Bearer <JWT>
    API->>Supa: Verify JWT token
    Supa-->>API: ✅ Valid, user ID = xyz789
    API->>DB: INSERT INTO users (id, name, email, phone, role='student')
    DB-->>API: ✅ User row created
    API-->>Browser: { user: { id, name, email, role } }

    Note over Browser: Redirect to menu page
```

---

## 4. Browsing Menu and Placing an Order

The main flow — student picks food and places an order.

```mermaid
sequenceDiagram
    actor Student
    participant Browser as Frontend (Browser)
    participant API as Flask API
    participant DB as PostgreSQL (Supabase)
    participant TG as Telegram Bot API
    participant Admin as Admin's Telegram

    Note over Student,Browser: === BROWSING MENU ===

    Student->>Browser: Opens menu page
    Browser->>API: GET /api/menu/stalls
    API->>DB: SELECT * FROM food_stalls WHERE is_active = true
    DB-->>API: List of stalls
    API-->>Browser: [{ name: "South Indian Corner", ... }]

    Student->>Browser: Clicks on a stall
    Browser->>API: GET /api/menu/stalls/1/items
    API->>DB: SELECT * FROM menu_items WHERE stall_id = 1
    DB-->>API: List of menu items with image URLs
    API-->>Browser: [{ name: "Masala Dosa", price: 40, image_url: "...", ... }]

    Note over Student,Browser: === ADDING TO CART ===

    Student->>Browser: Clicks "Add to Cart" on Masala Dosa
    Note over Browser: Cart is stored in localStorage<br/>(no API call needed)

    Student->>Browser: Clicks "Add to Cart" on Idli
    Note over Browser: Cart updated in localStorage

    Note over Student,Browser: === PLACING ORDER ===

    Student->>Browser: Goes to cart, clicks "Place Order"
    Browser->>API: POST /api/orders<br/>{ stall_id: 1, items: [{item_id: 1, qty: 2}, {item_id: 3, qty: 1}] }<br/>Header: Authorization: Bearer <JWT>
    API->>DB: Verify menu items exist and are available
    DB-->>API: ✅ Items valid
    API->>DB: INSERT INTO orders (user_id, stall_id, total, status='pending')
    API->>DB: INSERT INTO order_items (order_id, item_id, qty, price)
    DB-->>API: ✅ Order #123 created

    API->>TG: POST /sendMessage<br/>{ chat_id: admin_tg_id,<br/>text: "New order #123 from Ramesh - ₹120" }
    TG-->>Admin: 📱 "New order #123 from Ramesh..."

    API-->>Browser: { order_id: 123, status: "pending", total: 120 }

    Note over Browser: Clear cart from localStorage<br/>Redirect to orders page
```

---

## 5. Admin Approves an Order (with Telegram Notification)

What happens when admin reviews and approves a pending order.

```mermaid
sequenceDiagram
    actor Admin
    participant Browser as Admin Dashboard (Browser)
    participant API as Flask API
    participant DB as PostgreSQL (Supabase)
    participant TG as Telegram Bot API
    participant Phone as Student's Telegram

    Admin->>Browser: Opens admin dashboard
    Browser->>API: GET /api/admin/orders/pending<br/>Header: Authorization: Bearer <admin JWT>
    API->>DB: Verify user role = 'admin'
    API->>DB: SELECT orders WHERE status = 'pending'
    DB-->>API: List of pending orders with student details
    API-->>Browser: [{ order_id: 123, student: "Ramesh", items: [...], total: 120 }]

    Admin->>Browser: Clicks "Approve" on order #123
    Browser->>API: POST /api/admin/orders/123/approve<br/>{ estimated_time: 15 }
    API->>DB: UPDATE orders SET status = 'approved' WHERE id = 123
    DB-->>API: ✅ Updated

    Note over API: Check if student has<br/>a telegram_id linked

    API->>DB: SELECT telegram_id FROM users WHERE id = (order's user_id)
    DB-->>API: telegram_id = "987654321"

    API->>TG: POST /sendMessage<br/>{ chat_id: "987654321",<br/>text: "✅ Order #123 approved! Ready in ~15 min." }
    TG-->>Phone: 📱 "✅ Order #123 approved!..."

    API-->>Browser: { order: {...}, message: "Order approved" }
    Note over Browser: Order moves from<br/>"Pending" to "Approved" list
```

---

## 6. Admin Adds a Menu Item (with Image Upload)

How an admin uploads a dish photo and creates a new menu item.

```mermaid
sequenceDiagram
    actor Admin
    participant Browser as Admin Dashboard (Browser)
    participant Storage as Supabase Storage
    participant API as Flask API
    participant DB as PostgreSQL (Supabase)

    Admin->>Browser: Fills form: name, price, description
    Admin->>Browser: Selects a dish photo from computer

    Note over Browser: === STEP 1: Upload Image ===

    Browser->>Storage: supabase.storage<br/>.from('menu-images')<br/>.upload('paneer-dosa.jpg', file)
    Storage-->>Browser: ✅ File uploaded

    Browser->>Storage: supabase.storage<br/>.from('menu-images')<br/>.getPublicUrl('paneer-dosa.jpg')
    Storage-->>Browser: Public URL:<br/>https://xyz.supabase.co/storage/v1/object/public/menu-images/paneer-dosa.jpg

    Note over Browser: === STEP 2: Create Menu Item ===

    Browser->>API: POST /api/admin/menu/items<br/>{ name: "Paneer Dosa",<br/>  price: 60,<br/>  stall_id: 1,<br/>  image_url: "https://xyz.supabase.co/..." }<br/>Header: Authorization: Bearer <admin JWT>

    API->>DB: Verify user role = 'admin'
    API->>DB: INSERT INTO menu_items<br/>(name, price, stall_id, image_url, ...)
    DB-->>API: ✅ Menu item created

    API-->>Browser: { item: { id: 15, name: "Paneer Dosa", ... } }

    Note over Browser: New item appears in menu list<br/>with the uploaded photo
```

### Why Upload Works This Way

```
❌ BAD:  Browser → Flask API → save file to disk
         (complex, needs file handling, storage limits)

✅ GOOD: Browser → Supabase Storage (direct upload)
         Browser → Flask API (just sends the URL string)
         Flask stores only the URL — zero file handling!
```

---

## 7. Complete Order Lifecycle

All the states an order goes through from start to finish.

```mermaid
stateDiagram-v2
    [*] --> Pending: Student places order

    Pending --> Approved: Admin approves
    Pending --> Rejected: Admin rejects (with reason)

    Approved --> Ready: Admin marks "Ready for Pickup"

    Ready --> Completed: Student picks up food,<br/>Admin marks complete

    Rejected --> [*]
    Completed --> [*]

    note right of Pending
        📱 Admin gets Telegram notification
        "New order from Ramesh - ₹120"
    end note

    note right of Approved
        📱 Student gets Telegram notification
        "Order approved! Ready in ~15 min"
    end note

    note right of Ready
        📱 Student gets Telegram notification
        "Order ready for pickup!"
    end note

    note right of Rejected
        📱 Student gets Telegram notification
        "Order rejected: Item not available"
    end note
```

---

## 8. Deployment Architecture

How code gets from your laptop to the live servers.

```mermaid
graph LR
    subgraph "Your Laptop"
        CODE["💻 Write Code"]
    end

    subgraph "GitHub"
        REPO["📁 Repository<br/>lbrce-campus-food-court"]
        ACTIONS["⚙️ GitHub Actions<br/>Builds Docker Image"]
        PAGES["🌐 GitHub Pages<br/>Serves frontend/"]
    end

    subgraph "Ubuntu Server"
        DOCKER["🐳 Docker Container<br/>Flask API on port 5000"]
    end

    subgraph "Supabase Cloud"
        SUPA["☁️ Database + Auth + Storage<br/>(already running, nothing to deploy)"]
    end

    CODE -- "git push" --> REPO
    REPO -- "triggers on push<br/>to api/**" --> ACTIONS
    ACTIONS -- "builds image,<br/>verifies it works" --> ACTIONS
    REPO -- "auto-deploys<br/>frontend/ folder" --> PAGES
    REPO -- "ansible deploy.yml<br/>(or manual docker run)" --> DOCKER
    DOCKER -- "connects to" --> SUPA
    PAGES -- "connects to" --> SUPA

    style CODE fill:#e3f2fd,stroke:#1565c0,color:#000
    style REPO fill:#f5f5f5,stroke:#424242,color:#000
    style ACTIONS fill:#fff3e0,stroke:#e65100,color:#000
    style PAGES fill:#e8f5e9,stroke:#2e7d32,color:#000
    style DOCKER fill:#fce4ec,stroke:#c62828,color:#000
    style SUPA fill:#f3e5f5,stroke:#6a1b9a,color:#000
```

### Deployment Steps (Simple Version)

```
1. Push code to GitHub          →  git push origin main
2. Frontend auto-deploys        →  GitHub Pages serves frontend/ folder
3. API deployed manually        →  SSH into server, docker build, docker run
   OR via Ansible               →  ansible-playbook deploy.yml
4. GitHub Actions               →  Automatically builds Docker image to verify it works
```

---

## 9. Database Relationships (ER Diagram)

How the database tables connect to each other.

```mermaid
erDiagram
    users {
        uuid id PK
        text name
        text email UK
        text phone
        text telegram_id
        text role "student or admin"
        timestamp created_at
    }

    food_stalls {
        serial id PK
        text name
        text description
        text image_url
        boolean is_active
        timestamp created_at
    }

    menu_items {
        serial id PK
        int stall_id FK
        text name
        text description
        decimal price
        text image_url "from Supabase Storage"
        text category "main, snack, beverage, dessert"
        boolean is_available
        timestamp created_at
    }

    orders {
        serial id PK
        uuid user_id FK
        int stall_id FK
        decimal total_amount
        text status "pending, approved, rejected, ready, completed"
        text rejection_reason
        int estimated_time "minutes"
        timestamp created_at
        timestamp updated_at
    }

    order_items {
        serial id PK
        int order_id FK
        int menu_item_id FK
        int quantity
        decimal price_at_order "price when order was placed"
    }

    users ||--o{ orders : "places"
    food_stalls ||--o{ menu_items : "has"
    food_stalls ||--o{ orders : "receives"
    orders ||--|{ order_items : "contains"
    menu_items ||--o{ order_items : "referenced in"
```

### Reading the Diagram

| Symbol      | Meaning                                                       |
| ----------- | ------------------------------------------------------------- |
| `PK`        | Primary Key — unique identifier for each row                  |
| `FK`        | Foreign Key — links to another table's PK                     |
| `UK`        | Unique Key — no duplicates allowed                            |
| `\|\|--o{`  | One-to-many: one user has many orders                         |
| `\|\|--\|{` | One-to-many (required): one order must have at least one item |

---

## How to Preview These Diagrams

1. **GitHub** — Push this file and open it on github.com. Mermaid diagrams render automatically.

2. **VS Code** — Install the extension: `Markdown Preview Mermaid Support`

   ```
   Extensions → Search "Mermaid" → Install "Markdown Preview Mermaid Support"
   Then: Cmd+Shift+V to preview this file
   ```

3. **Online** — Copy any diagram code block and paste it at [mermaid.live](https://mermaid.live)
