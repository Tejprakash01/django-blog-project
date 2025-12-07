# 📝 Django Blog Project (Blog + REST API)

A full-stack **Django Blog Application** with authentication, image uploads, modern UI, and REST API support.  
The same backend serves **HTML pages for users** and **JSON APIs for external clients**.

---

## 🚀 Features

### ✅ Blog (Frontend)
- User authentication (Login / Logout)
- Create blog posts from frontend
- Upload images with posts
- Display posts with images
- Modern responsive UI
- Secure POST-based logout (Django 5 compatible)

### ✅ REST API
- List blog posts in JSON
- Create posts via API
- Shared database with frontend
- Ready for React / Mobile apps

---

## 🧱 Tech Stack

- **Backend**: Django 5.x  
- **API**: Django REST Framework  
- **Database**: SQLite3  
- **Frontend**: HTML, CSS (custom modern design)  
- **Auth**: Django Authentication System  
- **Media**: Image uploads using `ImageField`

---


django_blog_project/
│
├── blog/ # Blog app (models, views, templates)
├── api/ # REST API app
├── blog_project/ # Project settings
├── media/ # Uploaded images (gitignored)
├── manage.py
├── requirements.txt
└── README.md## 📁 Project Structure


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Tejprakash01/django-blog-project.git
cd django-blog-project
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
http://127.0.0.1:8000/

🔐 Authentication Routes
URL	Description
/login/	Login page
/logout/	Logout (POST method)
/admin/	Django admin panel

panel
🌐 API Endpoints
Method	Endpoint	Description
GET	/api/posts/	List all blog posts
POST	/api/posts/	Create post (auth required)
