📝 Django Blog Project (API + UI)

A modern Django Blog Application that combines Django REST Framework (API) with Django Templates (UI).
Includes authentication, CRUD operations, likes, dark mode UI, and user profiles.

🚀 Features
✅ Authentication

User signup / login / logout

Protected routes

Profile pages

✅ Blog System

Create, edit, delete posts

Upload post images

View posts by author

Pagination support

✅ Likes System

Like / Unlike posts

Like count updates dynamically (toggle)

One like per user per post

✅ UI & UX

Clean modern UI

Dark mode support 🌙

Responsive layout (mobile friendly)

Centralized CSS styling

✅ API Support

REST API for posts and likes

Django REST Framework used

Can be consumed by frontend apps later

🏗 Project Structure
django_blog_api_project/
│
├── api/                     # REST API app
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── blog/                    # Main blog app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── signals.py
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   ├── create_post.html
│   │   ├── edit_post.html
│   │   ├── profile.html
│   │   └── login.html
│   └── static/blog/
│       └── style.css
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/                   # Uploaded images
├── staticfiles/             # Collected static files
├── db.sqlite3
├── manage.py
└── README.md

🛠 Tech Stack

Backend: Django, Django REST Framework

Frontend: Django Templates, HTML, CSS

Database: SQLite (can be swapped with PostgreSQL)

Auth: Django Auth System

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Tejprakash01/django-blog-project.git
cd django-blog-project

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies
pip install django djangorestframework

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver


Open browser:

http://127.0.0.1:8000/

🔐 Environment Settings

Key settings in settings.py:

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"

🔄 API Endpoints (Sample)
Method	Endpoint	Description
GET	/api/posts/	List posts
POST	/api/posts/	Create post
POST	/like/<id>/	Like/Unlike post
🌙 Dark Mode

Toggle button available in navbar

Uses CSS variables

Persists UI preference per session

📸 Media Handling

Image uploads supported

Stored in /media/

Served in development via Django

✅ Future Improvements

AJAX likes (no reload)

Comments system

Deployment (Render / Railway)

JWT Authentication for API

React / Next.js frontend
