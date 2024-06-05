# from models.doctors import DoctorSchedule, Doctor
import factory
import random
from faker import Faker
from roles.custom_providers import IndianPhoneNumberProvider
from ..models.pharmacy import Medicine, MedicineSold
from .patients import PatientFactory
from django.utils import timezone
from ..custom_provider import MedicineProvider

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)
fake.add_provider(MedicineProvider)


class MedicineFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.medicine)
    quantity_per_item = factory.Faker('random_int', min=1, max=100)
    count_of_item = factory.Faker('random_int', min=1, max=100)
    is_prescription_required = factory.Faker('boolean')
    class Meta:
        model = Medicine


class MedicineSoldFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    timestamp = factory.LazyFunction(timezone.now)
    class Meta:
        model = MedicineSold

    @factory.post_generation
    def medicines(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for medicine in extracted:
                self.medicines.add(medicine)



