from django.core.management.base import BaseCommand
from users.management.factories import UserFactory
from users.models import User


class Command(BaseCommand):
    help = 'Seed the database with user data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of users to create')

    def handle(self, *args, **options):
        count = options['count']

        self.stdout.write('Deleting old user data...')
        User.objects.all().delete()

        self.stdout.write(f'Creating {count} new users...')
        for _ in range(count):
            user = UserFactory()
            self.stdout.write(f'Created user: {user.username}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} users'))
