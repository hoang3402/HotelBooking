from rest_framework import serializers
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
