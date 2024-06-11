from rest_framework import viewsets
from .serializers import RoleSerializer
from .models import Role

from django.shortcuts import get_object_or_404
from ninja import Router
from .schemas import RolesSchema
from typing import List

class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    
    def get_queryset(self): 
        return Role.objects.all()
    
#ninja_urls

router = Router()

@router.get("/roles/", response=List[RolesSchema])
def list_users(request):
    users = Role.objects.all()
    return users

@router.post("", response=RolesSchema)
def create_role(request, data: RolesSchema):
    user = Role.objects.create(**data.dict())
    return user

@router.get("", response=RolesSchema)
def get_role(request, user_id: int):
    user = get_object_or_404(Role, id=id)
    return user

@router.put("", response=RolesSchema)
def update_role(request, user_id: int, data: RolesSchema):
    user = get_object_or_404(Role, id=id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()
    return user

@router.delete("")
def delete_role(request, user_id: int):
    user = get_object_or_404(Role, id=id)
    user.delete()
    return {"success": True}

    


