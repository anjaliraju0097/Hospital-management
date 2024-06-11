# views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer



from django.shortcuts import get_object_or_404
from ninja import Router
from .schemas import UserSchema
from typing import List


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   

    # def get_permissions(self):
    #     if self.action in ['create', 'list', 'retrieve', 'update', 'partial_update']:
    #         self.permission_classes = [IsAuthenticated]
    #     elif self.action == 'destroy':
    #         self.permission_classes = [IsAdminUser]
    #     return super(self.__class__, self).get_permissions()

#ninja api

router = Router()

@router.get("/users/", response=List[UserSchema])
def list_users(request):
    users = User.objects.all()
    return users

@router.post("/users/", response=UserSchema)
def create_user(request, data: UserSchema):
    user = User.objects.create(**data.dict())
    return user

@router.get("/users/{id}/", response=UserSchema)
def get_user(request, user_id: int):
    user = get_object_or_404(User, id=id)
    return user

@router.put("/users/{id}/", response=UserSchema)
def update_user(request, user_id: int, data: UserSchema):
    user = get_object_or_404(User, id=id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()
    return user

@router.delete("/users/{id}/")
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=id)
    user.delete()
    return {"success": True}
