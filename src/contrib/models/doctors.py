from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


SPECIALIZATION_CHOICES = (
    ("Cardiologist", "Cardiologist"),
    ("Orthopedic Surgeon", "Orthopedic Surgeon"),
    ("Pediatrician", "Pediatrician"),
    ("Dermatologist", "Dermatologist"),
    ("Neurologist", "Neurologist"),
    ("Gynecologist", "Gynecologist"),
    ("Oncologist", "Oncologist"),
    ("ENT Specialist", "ENT Specialist"),
    ("Urologist", "Urologist"),
    ("Endocrinologist", "Endocrinologist"),
    ("General", "General"),
)

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False, unique=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, default=None) 
    license_number = models.CharField(max_length=50)
    Phone = PhoneNumberField(null=False, blank=False, unique=True)
    def __str__(self):
        return str(self.email)


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    working_days_of_week = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return str(self.id)
