from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(10):
            user = User.objects.create(
                email=f'user_{i}@user.user',

                is_superuser=False,
                is_staff=False,
                is_active=True
            )

            user.set_password('123qwe456rty')
            user.save()
