from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "django-blog-project-pyvl.onrender.com",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]

# APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Blog + API
    "blog.apps.BlogConfig",
    "api",
    "rest_framework",

    # Media
    "cloudinary",
    "cloudinary_storage",

    # Realtime
    "channels",
    "chat",
]


# MIDDLEWARE 

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URL / TEMPLATE
ROOT_URLCONF = "blog_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "blog" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI / ASGI
WSGI_APPLICATION = "blog_project.wsgi.application"
ASGI_APPLICATION = "blog_project.asgi.application"   

# DATABASE
if os.getenv("RENDER"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "blogdb",
            "USER": "postgres",
            "PASSWORD": "admin",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }


# CHANNELS / REDIS
REDIS_URL = os.environ.get("REDIS_URL")

if REDIS_URL:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [REDIS_URL],
            },
        }
    }
else:
    # Local fallback (NO REDIS REQUIRED)
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }


# STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "blog" / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# MEDIA (CLOUDINARY)

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"




# AUTH
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"

#CSRF & SESSION FIX FOR RENDER

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"

CSRF_COOKIE_HTTPONLY = False

# Tell Django it is behind Render's HTTPS proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

USE_X_FORWARDED_HOST = True


# CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://django-blog-project-pyvl.onrender.com",
]


# DEFAULT
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTOMATIC SUPERUSER CREATION ON RENDER
if os.getenv("RENDER") == "true":
    os.system("python manage.py create_superuser")