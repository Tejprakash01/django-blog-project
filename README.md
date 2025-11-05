# 📝 Django Blog Project

A simple and elegant **Django-based Blog Application** that allows admins to create, edit, and manage blog posts from the **Django Admin Panel**, and automatically displays them on the **frontend** with the **title, image, date, time**, and **message/content**.

---

## 🚀 Features

- 🧑‍💻 **Admin Panel Integration** – Easily add, edit, or delete blog posts via the Django admin interface.  
- 🖼️ **Image Uploads** – Each post supports uploading a feature image (stored in the `/media/` directory).  
- 🗓️ **Automatic Timestamps** – Date and time of creation are automatically stored and displayed.  
- 💬 **Rich Text Support** – Blog messages or descriptions are dynamically rendered on the frontend.  
- 🎨 **Responsive Frontend** – Simple and clean UI to view all blogs with proper layout.

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x  
- **Frontend:** HTML, CSS (Bootstrap recommended)  
- **Database:** SQLite (default)  
- **Language:** Python 3.x  

---
## 📂 Project Structure
DjangoBlog/
│
├── blog/ # Blog app
│ ├── migrations/ # Database migrations
│ ├── templates/blog/ # HTML templates for frontend, CSS, JS, Images
│ ├── models.py # Blog model (title, content, image, date)
│ ├── views.py # Logic to display blogs
│ ├── admin.py # Register model for admin
│ └── urls.py # Blog app URLs
│
├── DjangoBlog/ # Main project directory
│ ├── settings.py # Django settings (MEDIA config, etc.)
│ ├── urls.py # Main URL routing
│
├── media/ # Uploaded blog images
├── db.sqlite3 # Default SQLite database
└── manage.py # Django management script

JUST COPY 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
localhost:8000
YOU ARE READY TO GO!!

