from rest_framework import serializers
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from polls.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'number_phone', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['role'] = 'user'

        if user.is_staff:
            token['role'] = 'staff'

        if user.is_superuser:
            token['role'] = 'admin'

        return token


def get_tokens_for_user(user):
    refresh = MyTokenObtainPairSerializer.get_token(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class StaffPermission(BasePermission):
    message = 'You can\'t access this endpoint.'

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'update', 'partial_update', 'create']:
            return request.user.is_staff
        else:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve', 'update', 'partial_update', 'create']:
            return request.user.is_staff
        else:
            return request.user.is_superuser


class AdminPermission(BasePermission):
    message = 'Only Admin can access this endpoint.'

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return True
        elif view.action == 'create':
            return request.user.is_authenticated() and request.user.is_superuser
        elif view.action in ['update', 'partial_update']:
            return request.user.is_authenticated() and (request.user.is_staff or request.user.is_superuser)
        else:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated():
            return False

        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['update', 'partial_update']:
            return obj == request.user.is_staff or request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False
