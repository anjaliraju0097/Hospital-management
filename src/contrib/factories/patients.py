# from models.doctors import DoctorSchedule, Doctor
import factory
import random
from faker import Faker
from roles.custom_providers import IndianPhoneNumberProvider
from ..models.patients import Patient, PatientDetail, Appointment, MedicalRecord, DoctorPrescribedMedicine
from .doctors import DoctorFactory
from datetime import datetime

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)

def timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')


def generate_blood_group():
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    return random.choice(blood_groups)

def generate_allergies():
    allergies_list = ['Peanuts', 'Shellfish', 'Penicillin', 'Pollen', 'Dust mites', 'Animal dander', 'Latex']
    return random.choice(allergies_list)

fake.add_provider(generate_blood_group)
fake.add_provider(generate_allergies)

class PatientFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: fake.name()[:20])
    address = factory.Faker('address')
    phone = factory.LazyAttribute(lambda o: f"{fake.indian_phone_number()}_{timestamp()}") 
    class Meta:
        model = Patient

class PatientDetailFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    age = factory.Faker('random_int', min=0, max=100)
    blood_group = factory.LazyFunction(generate_blood_group)
    allergies = factory.LazyFunction(generate_allergies)
    class Meta:
        model  = PatientDetail

class AppointmentFactory(factory.django.DjangoModelFactory):
    doctor = factory.SubFactory(DoctorFactory)
    patient = factory.SubFactory(PatientFactory)
    appointment_datetime = factory.Faker('date_time_this_month', after_now=True)
    is_done = factory.Faker('boolean')
    class Meta:
        model = Appointment

class MedicalRecordFactory(factory.django.DjangoModelFactory):
    appointment = factory.SubFactory(AppointmentFactory)
    record_date = factory.Faker('date_time_this_month', after_now=True)
    description = factory.Faker('text')
    class Meta:
        model = MedicalRecord

class DoctorPrescribedMedicineFactory(factory.django.DjangoModelFactory):
    appointment = factory.SubFactory(AppointmentFactory)

    @factory.post_generation
    def medicines(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for medicine in extracted:
                self.medicines.add(medicine)
    class Meta:
        model = DoctorPrescribedMedicine

