# 📝 Django Blog Project

A full-stack **Django Blog Application** with authentication, image uploads, REST API support, dark mode UI, and production deployment on **Render** using **Cloudinary** for media storage.

🔗 **Live Demo**: https://django-blog-project-pyl.onrender.com

---

## 🚀 Features

### ✅ Core Functionality
- User registration & login
- Create, edit & delete blog posts
- Image upload support (Cloudinary)
- User profile page
- Admin panel
- Search posts
- Like system
- Authentication-protected routes

### 🎨 UI
- Clean & modern UI
- Dark mode toggle
- Responsive design

### ⚙️ Backend
- Django (MTV architecture)
- Django REST Framework (API ready)
- Media handling with Cloudinary
- Secure environment variable usage

### 🚀 Deployment
- Deployed on **Render**
- Production-ready settings
- Gunicorn + WhiteNoise
- Static & media files handled correctly

---

## 🛠️ Tech Stack

**Backend**
- Python 3.12
- Django 4.2
- Django REST Framework
- Gunicorn

**Frontend**
- HTML5
- CSS3
- JavaScript

**Storage & Deployment**
- Cloudinary (media storage)
- Render (hosting)
- SQLite (development DB)

---

## 📂 Project Structure

django_blog_api_project/
│
├── api/ # REST API
├── blog/ # Blog app
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│
├── blog_project/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── static/ # CSS & static files
├── templates/ # HTML templates
├── media/ # Local uploads (dev only)
│
├── requirements.txt
├── runtime.txt
├── manage.py
└── README.md
---

## ⚙️ Environment Variables

Set the following environment variables in **Render** (or `.env` locally):


---

## 📦 Installation (Local Setup)

1️⃣ Clone the repository
```bash
git clone https://github.com/Tejprakash01/django-blog-project.git
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Start development server
python manage.py runserver


Open: http://127.0.0.1:8000/
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
🧪 API Endpoints (Sample)
GET    /api/posts/
POST   /api/posts/
GET    /api/posts/<id>/


Supports JSON responses and can be extended for frontend or mobile apps.

🔒 Authentication Flow

Login required for creating/editing posts

Users can only modify their own posts

Secure logout & profile access

🖼️ Image Upload Handling

Uses Cloudinary for persistent media storage

No dependency on local filesystem

Images served via Cloudinary CDN

✔️ Fully production-safe
✔️ Works on free Render tier

✅ Deployment Notes (Render)

Python version pinned via runtime.txt

Build command:

pip install -r requirements.txt && python manage.py collectstatic --noinput


Start command:

gunicorn blog_project.wsgi:application🧠 Lessons Learned

Production Django settings

Debugging 500 errors on deployment

Handling media in cloud environments

Environment-based configuration

Real-world deployment workflow

🚧 Future Improvements

Pagination

Comments system

Email verification

API authentication (JWT)

PostgreSQL database

Docker support
