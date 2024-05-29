from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from roles.models import Role


class User(AbstractUser):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True)
    role = models.ForeignKey(Role,related_name='role', on_delete=models.CASCADE,null=True,blank=True)
    phone = PhoneNumberField(blank=False,null=False,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'role_id', "phone_number"]
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'












        