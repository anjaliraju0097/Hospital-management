from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    def __str__(self):
        return str(self.name)

    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_date = models.DateTimeField()
    description = models.TextField()
    def __str__(self):
        return str(self.id)
