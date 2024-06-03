# from models.doctors import DoctorSchedule, Doctor
import factory
import random
from faker import Faker
from roles.custom_providers import IndianPhoneNumberProvider
from ..models.pharmacy import Medicine, MedicineSold

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)


class MedicineFactory(factory.django.DjangoModelFactory):
    pass


class MedicineSoldFactory(factory.django.DjangoModelFactory):
    pass



