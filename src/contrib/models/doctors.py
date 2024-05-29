from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False, unique=True)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    Phone = PhoneNumberField(null=False, blank=False, unique=True)


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    working_days_of_week = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
