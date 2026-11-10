
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create an admin user if one does not already exist"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            raise CommandError(
                "Set DJANGO_SUPERUSER_USERNAME and "
                "DJANGO_SUPERUSER_PASSWORD environment variables."
            )

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Admin user already exists.")
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Admin user created successfully.")
        )
