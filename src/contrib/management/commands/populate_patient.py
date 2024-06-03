# File: src/contrib/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from ...factories.patients import PatientFactory, PatientDetailFactory, AppointmentFactory, MedicalRecordFactory, DoctorPrescribedMedicineFactory
from contrib.models import Medicine  # Ensure you have the Medicine model imported

class Command(BaseCommand):
    help = 'Populates the database with fake data for testing'

    def add_arguments(self, parser):
        parser.add_argument('total_patients', type=int, help='Number of patients to create')
        parser.add_argument('total_appointments', type=int, help='Number of appointments to create per patient')
        parser.add_argument('total_medicines', type=int, help='Number of prescribed medicines to create per appointment')

    def handle(self, *args, **kwargs):
        total_patients = kwargs['total_patients']
        total_appointments = kwargs['total_appointments']
        total_medicines = kwargs['total_medicines']

        for _ in range(total_patients):
            patient = PatientFactory.create()
            PatientDetailFactory.create(patient=patient)
            for _ in range(total_appointments):
                appointment = AppointmentFactory.create(patient=patient)
                MedicalRecordFactory.create(appointment=appointment)
                DoctorPrescribedMedicineFactory.create(appointment=appointment, medicines=[Medicine.objects.create() for _ in range(total_medicines)])

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))
