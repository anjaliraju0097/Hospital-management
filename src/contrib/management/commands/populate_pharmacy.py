from django.core.management.base import BaseCommand
from ...factories.pharmacy import MedicineFactory, MedicineSoldFactory, PatientFactory
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument('num_medicines', type=int, help='Indicates the number of medicines to create')

    def handle(self, *args, **options):
        num_medicines = options['num_medicines']

        # Create sample Medicines
        medicines = [MedicineFactory() for _ in range(num_medicines)]
        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_medicines} Medicine instances.'))

        # Create sample Patients
        patients = [PatientFactory() for _ in range(5)]
        self.stdout.write(self.style.SUCCESS('Successfully created 5 Patient instances.'))

        # Create sample MedicineSold instances
        for _ in range(5):
            patient = random.choice(patients)
            sold_medicines = random.sample(medicines, random.randint(1, 5))
            MedicineSoldFactory(patient=patient, medicines=sold_medicines)

        self.stdout.write(self.style.SUCCESS('Successfully created 5 MedicineSold instances with random medicines.'))
