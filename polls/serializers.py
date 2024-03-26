from rest_framework import serializers

from polls.models import City, Country, Hotel, Room, RoomType, HotelFeatures, SpecificHotelFeature, Booking, Province, \
    Review


class FeatureNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = ['description']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Province
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = City
        fields = '__all__'


class ProvinceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    # rooms = RoomSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'phone_number', 'average_rating', 'email', 'image', 'city']


class CreateHotelSerializer(serializers.ModelSerializer):
    province = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all())

    class Meta:
        model = Hotel
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
    hotel = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    def get_hotel(self, obj):
        # obj đại diện cho instance Booking hiện tại
        return {
            'id': obj.hotel.id,
            'name': obj.hotel.name,
            'image': obj.hotel.image
        }

    def get_room(self, obj):
        return {
            'id': obj.room.id,
            'name': obj.room.name,
            'adults': obj.room.adults,
            'children': obj.room.children
        }

    class Meta:
        model = Booking
        # fields = '__all__'
        exclude = ['user']


class BookingDetailsSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class DetailRoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = ['id', 'name', 'description', 'adults', 'children', 'hotel', 'price', 'image', 'is_available',
                  'room_type']


class DetailHotelSerializer(serializers.ModelSerializer):
    features = FeatureNameSerializer(many=True)
    room_set = DetailRoomSerializer(many=True)
    city = CitySerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'description', 'city', 'phone_number', 'average_rating', 'email',
                  'image', 'features', 'room_set']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class HotelFeaturesSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    feature = serializers.PrimaryKeyRelatedField(queryset=HotelFeatures.objects.all())

    class Meta:
        model = SpecificHotelFeature
        fields = ['hotel', 'feature']
