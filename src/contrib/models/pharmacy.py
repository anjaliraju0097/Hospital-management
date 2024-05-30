from django.db import models
import django.utils.timezone

from .doctors import Doctor
from .patients import Patient
from phonenumber_field.modelfields import PhoneNumberField


class Medicine(models.Model):
    name = models.CharField(max_length=20)
    quantity_per_item = models.IntegerField(default=0, blank=True)
    count_of_item = models.IntegerField(default=0, blank=True)
    is_prescription_required = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)


class MedicineSold(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medicines_sold')
    medicines = models.ManyToManyField(Medicine, blank=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.id)
