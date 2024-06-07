from django.db import models
import django.utils.timezone

from .doctors import Doctor
# from .pharmacy import Medicine
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    def __str__(self):
        return str(self.id)
    
class PatientDetail(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, related_name='patient_detail')
    age = models.IntegerField(default=0, blank=True)
    blood_group = models.CharField(max_length=3)
    allergies = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointment')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointment')
    appointment_datetime = models.DateTimeField(default=django.utils.timezone.now)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class MedicalRecord(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_records', null=True)
    record_date = models.DateTimeField()
    description = models.TextField()
    def __str__(self):
        return str(self.id)

class DoctorPrescribedMedicine(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescribed_medicines', null=True)
    medicines = models.ManyToManyField('contrib.Medicine', blank=True)
    # medicines = models.ManyToManyField(Medicine, blank=True)
    def __str__(self):
        return str(self.id)
