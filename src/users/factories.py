import factory
from .models import User
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')
    role = factory.Faker('role')
    phone = factory.Faker('phone')
    class Meta:
        model = User
   
    