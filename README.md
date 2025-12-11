🌐 Django Blog Project

A full-stack Django Blog Application with:

Django REST Framework API

Authentication (Login, Register, Logout)

PostgreSQL database (Render Cloud)

Cloudinary media storage (Images)

Django Template UI with modern styling

CRUD operations for posts

Likes, Profiles, Dark Mode

Fully deployed on Render

🚀 Live Demo

🔗 https://django-blog-project-pvyl.onrender.com

📸 Features
🔐 Authentication

Register

Login

Logout

Redirect to login when unauthorized

✍️ Blog

Create, edit, delete posts

Upload images (Cloudinary)

Styled blog UI with search

❤️ Interactions

Like posts

User profiles

⚙️ Backend API

Django REST Framework

Token-ready endpoints

☁️ Deployment Architecture

Render Web Service → App server

PostgreSQL Cloud DB → Persistent storage

Cloudinary → Media hosting (images)

Gunicorn + WhiteNoise → Production optimized

🛠️ Tech Stack
Component	Technology
Backend	Django, Django REST Framework
Database	PostgreSQL (Render Cloud)
Media Storage	Cloudinary
Frontend	Django Templates, HTML/CSS
Deployment	Render
Server	Gunicorn
Static Files	WhiteNoise
📂 Project Structure
project/
│
├── api/                # DRF API
├── blog/               # Templates + UI + Views
├── blog_project/       # Settings, URLs, WSGI
│
├── static/             # CSS files
├── media/              # Cloudinary-managed
│
├── requirements.txt
├── runtime.txt         # Python version
├── manage.py
└── README.md

🧰 Environment Variables (Render)

Make sure to add these in Render ➝ Environment:

Cloudinary
CLOUDINARY_CLOUD_NAME=xxxx
CLOUDINARY_API_KEY=xxxx
CLOUDINARY_API_SECRET=xxxx

PostgreSQL (Render Database)
DB_NAME=render_db_name
DB_USER=render_db_user
DB_PASSWORD=render_db_password
DB_HOST=render_db_host
DB_PORT=5432

Render Flag
RENDER=True


This allows settings.py to auto-switch between Local & Production.

⚙️ Local Development Setup
1️⃣ Clone the project
git clone https://github.com/Tejprakash01/django-blog-project.git
cd django-blog-project

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add .env file (local)
DB_NAME=blogdb
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432

4️⃣ Run migrations
python manage.py migrate

5️⃣ Start server
python manage.py runserver

☁️ Deployment Guide (Render)
1. Create a Web Service

Connect your GitHub repo

Select Python / Django

Add build command:

pip install -r requirements.txt


Add start command:

gunicorn blog_project.wsgi:application

2. Add Environment Variables

Paste all variables listed earlier.

3. Add PostgreSQL Database on Render

Add new → PostgreSQL

Copy credentials into Render environment variables.

4. Deploy

Render detects new commits automatically.

🖼️ Image Uploads

Images use Cloudinary:

No local media needed

Perfect for Render free tier

Auto optimization

📌 Important Notes

Render free tier sleeps after inactivity (≈50s wake-up delay).

PostgreSQL maintains your data — no resetting.

Cloudinary stores images permanently.

🤝 Contributing

Pull requests are welcome!
Please open an issue to discuss major changes.

📜 License

This project is open-source under the MIT License.

💬 Author

👨‍💻 Tej Prakash Tak
GitHub: https://github.com/Tejprakash01
