from rest_framework import serializers

from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','role_name','status']

    def validate_role_name(self, value):
        if Role.objects.filter(role_name=value).exists():
            raise serializers.ValidationError("This role name already exists.")
        return value    