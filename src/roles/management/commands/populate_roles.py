from django.core.management.base import BaseCommand
from ...factories import RoleFactory

class Command(BaseCommand):
    help = 'Populates the database with fake Role data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of roles to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            RoleFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} roles'))
