from rest_framework import serializers

from .models.doctors import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'specialization', 'license_number', 'Phone']