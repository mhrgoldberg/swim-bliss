from django.core.management import call_command
from django.core.management.base import BaseCommand
from locations.management.factories import LocationFactory
from locations.models import Location
from users.models import User


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of locations to create')

    def handle(self, *args, **options):
        count = options['count']

        # Seed users first
        self.stdout.write('Seeding users...')
        call_command('seed_users', count=10)  # Adjust count as needed

        # Fetch users to use for created_by field
        users = list(User.objects.all())

        self.stdout.write('Deleting old data...')
        Location.objects.all().delete()

        self.stdout.write('Creating new locations...')

        # Create locations
        for _ in range(count):
            user = users[_ % len(users)]  # Cycle through users
            location = LocationFactory(created_by=user)
            self.stdout.write(f'Created location: {location.name}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} locations'))
