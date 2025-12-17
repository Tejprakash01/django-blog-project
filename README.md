# 📝 Django Blog Project with Real-Time Chat (BOCHA)

A full-stack Django web application featuring a blogging platform with user authentication and **real-time private chat** using **Django Channels + WebSockets + Redis**.

Deployed on **Render** with PostgreSQL and Redis.

---

## 🚀 Live Demo

**👉 https://django-blog-project-pvyl.onrender.com/

---

## ✨ Features

### 🔐 Authentication
- User registration & login
- Secure logout (CSRF protected)
- Profile pages

### 📰 Blog
- Create, edit, delete posts
- Comment system
- User-based permissions

### 💬 Real-Time Chat
- One-to-one private chat
- Chat request & approval system
- Real-time messaging using WebSockets
- Message persistence in database
- No page reload required

### 🌙 UI
- Light / Dark mode
- Clean, responsive layout

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django |
| **API** | Django REST Framework |
| **Realtime** | Django Channels |
| **WebSockets** | Daphne |
| **Message Broker** | Redis |
| **Database** | PostgreSQL |
| **Static Files** | WhiteNoise |
| **Media Storage** | Cloudinary |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | Render |

---

## 📁 Project Structure

```
django-blog-project/
│
├── blog/                    # Blog app
├── chat/                    # Chat app (Channels)
├── api/                     # REST APIs
├── blog_project/            # Main project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/                  # Static files
├── templates/               # HTML templates
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Variables (Render)

Set these in **Render → Environment**:

```env
SECRET_KEY=your-secret-key
DEBUG=False
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=********
DB_HOST=********
DB_PORT=5432
REDIS_URL=redis://red-xxxxx:6379
CLOUDINARY_CLOUD_NAME=xxxx
CLOUDINARY_API_KEY=xxxx
CLOUDINARY_API_SECRET=xxxx
RENDER=true
```

---

## 🧩 Local Setup (Development)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Tejprakash01/django-blog-project.git
cd django-blog-project
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py migrate
```

### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Start Redis (Required for Chat)
```bash
redis-server
```

### 7️⃣ Run server
```bash
python manage.py runserver
```

**Open 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔌 WebSocket Architecture

- **Protocol:** `ws://` (local) / `wss://` (production)
- **Consumer:** `ChatConsumer`
- **Channel Layer:** Redis
- **ASGI Server:** Daphne

```
Client (Browser)
      ↓ WebSocket
Daphne (ASGI)
      ↓
   Channels
      ↓
    Redis
```

---

## 🧠 Chat Models

```python
ChatRequest  # Request & approval system
ChatRoom     # One-to-one room
Message      # Persistent messages
```

---

## 🔐 Security

- ✅ CSRF protection enabled
- ✅ Secure cookies
- ✅ AuthMiddlewareStack for WebSockets
- ✅ Allowed hosts restricted
- ✅ HTTPS + WSS in production

---

## 📦 Deployment Notes (Render)

- Uses **Daphne**, not Gunicorn
- **Redis is mandatory** for chat
- **PostgreSQL** for production DB
- Static files served via **WhiteNoise**

---

## 🧑‍💻 Author

**Tej Prakash Tak**

**GitHub:** [@Tejprakash01](https://github.com/Tejprakash01)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


---

## ⭐ Show your support

Give a ⭐️ if this project helped you!
