import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create superuser automatically (Render free compatible, no email)"

    def handle(self, *args, **kwargs):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        # If env variables are missing, do nothing
        if not username or not password:
            self.stdout.write("Superuser env variables not set")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("Superuser already exists")
            return

        # Create superuser
        User.objects.create_superuser(
            username=username,
            password=password
        )

        self.stdout.write("Superuser created successfully")
