from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from .models import User, Role



class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role  # Assuming this is your Role model
        fields = ['id', 'name', 'permissions']


class UserSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='role', write_only=True, allow_null=True, required=False)
    role_details = serializers.SerializerMethodField()  # Ensure this is included

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'role', 'role_id', 'role_details')  # Add 'role_details' here
        extra_kwargs = {'password': {'write_only': True}}

    def get_role_details(self, obj):
        if obj.role:  # Ensure this logic correctly fetches the role
            role_serializer = RoleSerializer(obj.role)
            return role_serializer.data
        return None

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        user = super().create(validated_data)
        return user