import factory
from .models import Role
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    role_name = factory.Faker('role_name')
    status = factory.Faker('status')
    class Meta:
        model = Role
 
