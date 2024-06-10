from django.core.management.base import BaseCommand
# from factories.doctors import DoctorFactory, DoctorScheduleFactory
from ...factories.doctors import DoctorFactory, DoctorScheduleFactory

class Command(BaseCommand):
    help = 'Populates the database with fake Doctor and DoctorSchedule data'

    def add_arguments(self, parser):
        parser.add_argument('total_doctors', type=int, help='Number of fake doctors to create')
        parser.add_argument('total_schedules_per_doctor', type=int, help='Number of fake schedules per doctor')

    def handle(self, *args, **kwargs):
        total_doctors = kwargs['total_doctors']
        total_schedules_per_doctor = kwargs['total_schedules_per_doctor']

        for _ in range(total_doctors):
            doctor = DoctorFactory.create()
            DoctorScheduleFactory.create_batch(total_schedules_per_doctor, doctor=doctor)
        self.stdout.write(self.style.SUCCESS('Successfully populated data'))
