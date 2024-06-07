import factory
from .models import Role
from users.models import User
from faker import Faker
from .custom_providers import IndianPhoneNumberProvider
from datetime import datetime

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)

def timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')

class RoleFactory(factory.django.DjangoModelFactory):
    role_name = factory.LazyAttribute(lambda o: f"{fake.job()[:100 - 21]}_{timestamp()}") 
    status = factory.Faker('boolean')
    class Meta:
        model = Role

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda o: f"{fake.unique.user_name()}_{timestamp()}") 
    name = factory.LazyAttribute(lambda o: fake.name()[:15]) 
    email = factory.LazyAttribute(lambda o: f"{fake.unique.email().split('@')[0]}_{timestamp()}@{fake.unique.email().split('@')[1]}")
    role = factory.SubFactory(RoleFactory)
    phone = factory.LazyAttribute(lambda o: f"{fake.indian_phone_number()}{timestamp()}") 
    class Meta:
        model = User        


 
 
