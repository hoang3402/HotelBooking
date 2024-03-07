from rest_framework import serializers

from polls.models import City, Country, Hotel, Room, RoomType, HotelFeatures, SpecificHotelFeature, Booking


class FeatureNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = ['description']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ['name', 'country']


class HotelSerializer(serializers.ModelSerializer):
    city = CityDetailSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'phone_number', 'average_rating', 'email', 'image', 'city']


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


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingDetailsSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class DetailRoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = ['id', 'name', 'description', 'adults', 'children', 'hotel', 'price', 'image', 'is_available', 'room_type']


class DetailHotelSerializer(serializers.ModelSerializer):
    city = CityDetailSerializer()
    features = FeatureNameSerializer(many=True)
    room_set = DetailRoomSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'description', 'phone_number', 'average_rating', 'email', 'image', 'city',
                  'features', 'room_set']
