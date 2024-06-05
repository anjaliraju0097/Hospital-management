import factory
from .models import Role
from users.models import User

from faker import Faker
from .custom_providers import IndianPhoneNumberProvider

fake = Faker()
fake.add_provider(IndianPhoneNumberProvider)

class RoleFactory(factory.django.DjangoModelFactory):
    role_name = factory.LazyAttribute(lambda o: fake.unique.job()) 
    status = factory.Faker('boolean')
    class Meta:
        model = Role


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda o: fake.unique.user_name())  # Ensure unique username
    name = factory.LazyAttribute(lambda o: fake.name()[:15]) # generated names do not exceed 15 characters , the maxlength = 15 in user model for name
    email = factory.LazyAttribute(lambda o: fake.unique.email())
    role = factory.SubFactory(RoleFactory)
    phone = factory.LazyAttribute(lambda o: fake.indian_phone_number())
    
    class Meta:
        model = User        


 
 
