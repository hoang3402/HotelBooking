from rest_framework import serializers

from polls.models import City, Country, Hotel, Room, RoomType, HotelFeatures, SpecificHotelFeature


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = '__all__'


class SpecificHotelFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificHotelFeature
        fields = '__all__'
