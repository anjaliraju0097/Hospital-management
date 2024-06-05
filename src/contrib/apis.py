# from django.shortcuts import get_object_or_404

# third party
# from rest_framework.exceptions import NotFound
# from rest_framework.serializers import ValidationError
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.db.models import F, Max

# from core.renderer import custom_renderer

from .models import AuditTaskUser, AuditTask, AssetCondition, AuditStatus

# from .serializers import AuditTaskUserSerializer,AuditTaskSerializer,AssetSerializer,AuditTaskUserGetSerializer,AssetDetailUpdateSerializer,AssetConditionSerializer


def f(msg):
    return Response(data={"detail": str(msg)})


class AuditTaskViewSet(viewsets.ModelViewSet):
    # serializer_class = AuditTaskUserSerializer
    queryset = AuditTaskUser.objects.filter(is_delete=False)


    def get_queryset(self):
        queryset = AuditTaskUser.objects.filter(
            is_delete=False,
            audit_plant_code__in=self.request.user.plant.all()
        ).exclude(audit_task__audit_status=AuditStatus.CLOSED).order_by('-id')
        
        distinct_queryset = queryset.values('audit_plant_code', 'audit_task').annotate(
            max_id=Max('id')
        ).values('max_id')
        
        return queryset.filter(id__in=distinct_queryset)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuditTaskUserGetSerializer
        else:
            return AuditTaskUserSerializer
    
