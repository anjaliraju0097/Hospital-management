# from models.doctors import DoctorSchedule, Doctor
import factory
import random
from faker import Faker
from roles.custom_providers import IndianPhoneNumberProvider
from ..models.doctors import Doctor, DoctorSchedule
from datetime import datetime

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)


def timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')

# custom function to generate doctor specialization
def generate_specialization():
    specializations = ['Cardiologist', 'Orthopedic Surgeon', 
                       'Pediatrician', 'Dermatologist', 'Neurologist',
                         'Gynecologist', 'Oncologist', 'ENT Specialist', 
                         'Urologist', 'Endocrinologist', 'General']
    return random.choice(specializations)

class DoctorFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: fake.name()[:15]) 
    email = factory.LazyAttribute(lambda o: f"{fake.unique.email()}_{timestamp()}")
    specialization = factory.LazyFunction(generate_specialization) 
    license_number = factory.LazyAttribute(lambda o: f"{fake.unique.ssn()}_{timestamp()}") 
    Phone = factory.LazyAttribute(lambda o: f"{fake.indian_phone_number()}_{timestamp()}") 
    class Meta:
        model = Doctor        


class DoctorScheduleFactory(factory.django.DjangoModelFactory):
    doctor = factory.SubFactory(DoctorFactory)
    working_days_of_week = factory.LazyFunction(lambda: random.randint(1, 7))
    start_time = factory.Faker('date_time_this_month', after_now=True)
    end_time = factory.Faker('date_time_between', start_date='now', end_date='+1y')
    class Meta:
        model = DoctorSchedule


