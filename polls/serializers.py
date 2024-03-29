from rest_framework import serializers

from .models import Hotel, User


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'number_phone', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
