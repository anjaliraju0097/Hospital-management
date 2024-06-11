# ninja
from typing import List
from ninja import NinjaAPI, Schema

# drf
from rest_framework import viewsets

from .models.doctors import Doctor
from .serializers import DoctorSerializer


# ninja
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.prefetch_related('schedules')
        specialization = self.request.query_params.get('specialization') or None
        if not specialization == None:
            queryset =queryset.filter(specialization=specialization)
        return queryset


# drf
api = NinjaAPI()
class DoctorScheme(Schema):
    id: int
    name: str
    email: str
    specialization: str
    license_number: str
    # Phone: str


@api.get("doctors/", response=List[DoctorScheme])
def doctors(request, specialization: str=None):
    queryset = Doctor.objects.all()
    if not specialization == None:
        queryset = Doctor.objects.filter(specialization=specialization)
    return queryset
