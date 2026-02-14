# API Specification

## Base URL

```
http://localhost:5000/api
```

## Authentication

All protected endpoints require the header:

```
Authorization: Bearer <supabase_jwt_token>
```

The JWT token is obtained from Supabase Auth after login/register. The backend verifies this token against Supabase to identify the user.

---

## Auth Endpoints

> Supabase handles auth internally; these routes proxy to Supabase Auth for consistency.

### Register

```
POST /auth/register
```

**Body:**

```json
{
  "email": "student@lbrce.edu.in",
  "password": "mypassword",
  "name": "Ramesh Kumar",
  "phone": "9876543210"
}
```

**Response (201):**

```json
{
  "user": { "id": "uuid", "email": "student@lbrce.edu.in" },
  "session": { "access_token": "...", "refresh_token": "..." }
}
```

### Login

```
POST /auth/login
```

**Body:**

```json
{
  "email": "student@lbrce.edu.in",
  "password": "mypassword"
}
```

**Response (200):**

```json
{
  "user": { "id": "uuid", "email": "student@lbrce.edu.in" },
  "session": { "access_token": "...", "refresh_token": "..." }
}
```

### Logout

```
POST /auth/logout
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{ "message": "Logged out" }
```

---

## User Endpoints

### Get Profile

```
GET /users/profile
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{
  "id": "uuid",
  "name": "Ramesh Kumar",
  "email": "student@lbrce.edu.in",
  "phone": "9876543210",
  "telegram_id": null,
  "role": "student"
}
```

### Update Profile

```
PUT /users/profile
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{
  "name": "Ramesh K",
  "phone": "9876543210",
  "telegram_id": "123456789"
}
```

**Response (200):**

```json
{
  "user": {
    "id": "uuid",
    "name": "Ramesh K",
    "phone": "9876543210",
    "telegram_id": "123456789",
    "role": "student"
  }
}
```

---

## Menu Endpoints

### List Food Stalls

```
GET /menu/stalls
```

**Response (200):**

```json
[
  {
    "id": 1,
    "name": "South Indian Corner",
    "description": "Authentic South Indian breakfast and snacks",
    "image_url": "",
    "is_active": true
  },
  {
    "id": 2,
    "name": "Juice & Snacks Bar",
    "description": "Fresh juices, sandwiches, and quick bites",
    "image_url": "",
    "is_active": true
  }
]
```

### List Menu Items for a Stall

```
GET /menu/stalls/:stall_id/items
Query params: ?category=main (optional)
```

**Response (200):**

```json
[
  {
    "id": 1,
    "stall_id": 1,
    "name": "Masala Dosa",
    "description": "Crispy dosa with potato filling",
    "price": 40.0,
    "image_url": "https://xyz.supabase.co/storage/v1/object/public/menu-images/masala-dosa.jpg",
    "category": "main",
    "is_available": true
  }
]
```

### Get Single Menu Item

```
GET /menu/items/:item_id
```

**Response (200):**

```json
{
  "id": 1,
  "name": "Masala Dosa",
  "description": "Crispy dosa with potato filling",
  "price": 40.0,
  "image_url": "https://xyz.supabase.co/storage/v1/object/public/menu-images/masala-dosa.jpg",
  "category": "main",
  "is_available": true
}
```

### Search Menu

```
GET /menu/search?q=dosa
```

**Response (200):**

```json
[
  {
    "id": 1,
    "name": "Masala Dosa",
    "description": "Crispy dosa with potato filling",
    "price": 40.0,
    "image_url": "",
    "category": "main",
    "is_available": true,
    "stall_name": "South Indian Corner"
  }
]
```

---

## Order Endpoints

### Place Order

```
POST /orders
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{
  "stall_id": 1,
  "items": [
    { "menu_item_id": 1, "quantity": 2 },
    { "menu_item_id": 3, "quantity": 1 }
  ]
}
```

**Response (201):**

```json
{
  "order_id": 123,
  "total_amount": 105.0,
  "status": "pending",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### List My Orders

```
GET /orders
Headers: Authorization: Bearer <token>
Query params: ?status=pending (optional)
```

**Response (200):**

```json
[
  {
    "id": 123,
    "stall": { "id": 1, "name": "South Indian Corner" },
    "items": [
      {
        "menu_item": { "id": 1, "name": "Masala Dosa", "image_url": "" },
        "quantity": 2,
        "price_at_order": 40.0
      }
    ],
    "total_amount": 105.0,
    "status": "pending",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
]
```

### Get Single Order

```
GET /orders/:order_id
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{
  "id": 123,
  "stall": { "id": 1, "name": "South Indian Corner" },
  "items": [
    {
      "menu_item": { "id": 1, "name": "Masala Dosa", "image_url": "" },
      "quantity": 2,
      "price_at_order": 40.0
    }
  ],
  "total_amount": 105.0,
  "status": "pending",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

---

## Admin Endpoints

> All admin endpoints require `Authorization` header and user must have `role = 'admin'`.

### Get Pending Orders

```
GET /admin/orders/pending
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
[
  {
    "id": 123,
    "user": { "name": "Ramesh Kumar", "phone": "9876543210" },
    "stall": { "id": 1, "name": "South Indian Corner" },
    "items": [...],
    "total_amount": 105.00,
    "status": "pending",
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

### List All Orders (with filters)

```
GET /admin/orders
Headers: Authorization: Bearer <token>
Query params: ?status=approved&date=2024-01-15 (optional)
```

**Response (200):**

```json
[{ "...all orders matching filters..." }]
```

### Approve Order

```
POST /admin/orders/:order_id/approve
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{ "estimated_time": 15 }
```

**Response (200):**

```json
{
  "order": { "id": 123, "status": "approved", "estimated_time": 15 },
  "message": "Order approved"
}
```

### Reject Order

```
POST /admin/orders/:order_id/reject
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{ "reason": "Item not available" }
```

**Response (200):**

```json
{
  "order": {
    "id": 123,
    "status": "rejected",
    "rejection_reason": "Item not available"
  },
  "message": "Order rejected"
}
```

### Mark Order Ready

```
POST /admin/orders/:order_id/ready
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{
  "order": { "id": 123, "status": "ready" },
  "message": "Order marked as ready"
}
```

### Complete Order

```
POST /admin/orders/:order_id/complete
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{
  "order": { "id": 123, "status": "completed" },
  "message": "Order completed"
}
```

### Add Menu Item

```
POST /admin/menu/items
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{
  "stall_id": 1,
  "name": "Paneer Dosa",
  "description": "Dosa with paneer filling",
  "price": 60.0,
  "category": "main",
  "image_url": "https://xyz.supabase.co/storage/v1/object/public/menu-images/paneer-dosa.jpg"
}
```

**Response (201):**

```json
{
  "item": {
    "id": 11,
    "stall_id": 1,
    "name": "Paneer Dosa",
    "price": 60.0,
    "image_url": "https://xyz.supabase.co/storage/v1/object/public/menu-images/paneer-dosa.jpg",
    "category": "main",
    "is_available": true
  }
}
```

### Update Menu Item

```
PUT /admin/menu/items/:item_id
Headers: Authorization: Bearer <token>
```

**Body:**

```json
{ "price": 70.0, "is_available": false }
```

**Response (200):**

```json
{
  "item": { "id": 1, "price": 70.0, "is_available": false }
}
```

### Delete Menu Item

```
DELETE /admin/menu/items/:item_id
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{ "message": "Item deleted" }
```

### Get Admin Stats

```
GET /admin/stats
Headers: Authorization: Bearer <token>
```

**Response (200):**

```json
{
  "today_orders": 45,
  "pending_orders": 3,
  "today_revenue": 2500.0,
  "popular_items": [
    { "name": "Masala Dosa", "count": 12 },
    { "name": "Filter Coffee", "count": 9 }
  ]
}
```

---

## Telegram Notifications (Internal)

Notifications are **not** API endpoints. They are called internally by the route handlers when order status changes.

The function in `api/services/telegram.py` calls:

```
POST https://api.telegram.org/bot<TOKEN>/sendMessage
Body: { "chat_id": <user_telegram_id>, "text": "<message>" }
```

**Student Notification Messages:**

- Order approved: `"Your order #123 has been approved! It will be ready in 15 minutes."`
- Order ready: `"Your order #123 is ready for pickup at South Indian Corner!"`
- Order rejected: `"Your order #123 was rejected. Reason: Item not available."`

**Admin Notification Messages:**

- New order: `"New order #123 from Ramesh Kumar - South Indian Corner - ₹80"`

---

## Error Responses

All errors follow this format:

```json
{
  "error": "Description of what went wrong"
}
```

**Common Status Codes:**

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden (not admin) |
| 404  | Not Found             |
| 500  | Server Error          |

---

## Image Upload Flow

Images are **not** uploaded through the API. The frontend uploads images directly to Supabase Storage:

1. Admin selects image file in the browser
2. Frontend JS uploads to Supabase Storage bucket `menu-images` using the Supabase JS client
3. Supabase returns the public URL
4. Frontend sends that URL as the `image_url` field in the API request body (POST/PUT)
5. API just stores the URL string — no file handling needed
