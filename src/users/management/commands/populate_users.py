from django.core.management.base import BaseCommand
from roles.factories import UserFactory 

class Command(BaseCommand):
    help = 'Populates the database with fake User data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            UserFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} users'))
