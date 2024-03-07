from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from HotelBooking.settings import API_KEY_EXCHANGE_CURRENCY
from polls.serializers import *
from polls.utilities import is_room_available, calculate_total_cost, get_exchange_rate


# Hotel

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_list_view = HotelViewSet.as_view({'get': 'list'})
# hotel_detail_view = HotelViewSet.as_view({'get': 'retrieve'})
hotel_create_view = HotelViewSet.as_view({'post': 'create'})
hotel_edit_view = HotelViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
hotel_delete_view = HotelViewSet.as_view({'delete': 'destroy'})


class HotelDetailRoomViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = DetailHotelSerializer


hotel_detail_view = HotelDetailRoomViewSet.as_view({'get': 'retrieve'})


# Room

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


room_list_view = RoomViewSet.as_view({'get': 'list'})
room_detail_view = RoomViewSet.as_view({'get': 'retrieve'})
room_create_view = RoomViewSet.as_view({'post': 'create'})
room_edit_view = RoomViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
room_delete_view = RoomViewSet.as_view({'delete': 'destroy'})


# RoomType

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


room_type_list_view = RoomTypeViewSet.as_view({'get': 'list'})
room_type_create_view = RoomTypeViewSet.as_view({'post': 'create'})
room_type_edit_view = RoomTypeViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
room_type_delete_view = RoomTypeViewSet.as_view({'delete': 'destroy'})


# Feature

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = HotelFeatures.objects.all()
    serializer_class = FeatureSerializer


feature_list_view = FeatureViewSet.as_view({'get': 'list'})
feature_create_view = FeatureViewSet.as_view({'post': 'create'})
feature_edit_view = FeatureViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
feature_delete_view = FeatureViewSet.as_view({'delete': 'destroy'})


# Feature hotel

class FeatureHotelViewSet(viewsets.ModelViewSet):
    queryset = SpecificHotelFeature.objects.all()
    serializer_class = SpecificHotelFeatureSerializer

    def retrieve(self, *args, **kwargs):
        specific_hotel_features = SpecificHotelFeature.objects.filter(hotel=kwargs['pk'])
        serializer = SpecificHotelFeatureSerializer(specific_hotel_features, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


feature_hotel_list_view = FeatureHotelViewSet.as_view({'get': 'list'})
feature_hotel_detail_view = FeatureHotelViewSet.as_view({'get': 'retrieve'})
feature_hotel_create_view = FeatureHotelViewSet.as_view({'post': 'create'})
feature_hotel_edit_view = FeatureHotelViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
feature_hotel_delete_view = FeatureHotelViewSet.as_view({'delete': 'destroy'})


# City

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


city_list_view = CityViewSet.as_view({'get': 'list'})
city_create_view = CityViewSet.as_view({'post': 'create'})
city_edit_view = CityViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
city_delete_view = CityViewSet.as_view({'delete': 'destroy'})


# Country

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


country_list_view = CountryViewSet.as_view({'get': 'list'})
country_create_view = CountryViewSet.as_view({'post': 'create'})
country_edit_view = CountryViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
country_delete_view = CountryViewSet.as_view({'delete': 'destroy'})


# Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


booking_list_view = BookingViewSet.as_view({'get': 'list'})
booking_detail_view = BookingViewSet.as_view({'get': 'retrieve'})
booking_create_view = BookingViewSet.as_view({'post': 'create'})
booking_edit_view = BookingViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
booking_delete_view = BookingViewSet.as_view({'delete': 'destroy'})


class Search(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Get data from the POST request
        number_adults = request.data.get('adults', None)
        number_children = request.data.get('children', None)
        country_code = request.data.get('country', None)
        city_code = request.data.get('city', None)

        queryset = Hotel.objects.all()

        if number_adults:
            queryset = queryset.filter(room__adults__gte=number_adults)

        if number_children:
            queryset = queryset.filter(room__children__gte=number_children)

        if country_code:  # Update variable name
            queryset = queryset.filter(city__country__code=country_code)

        if city_code:
            queryset = queryset.filter(city__code=city_code)

        # Serialize the queryset
        serializer = HotelSerializer(queryset, many=True)

        # Return the serialized data as JSON response
        return Response(serializer.data)


search_view = Search.as_view()


class MakeBooking(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, hotel_id):
        user = request.user
        room_id = request.data.get('room_id')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')
        adults = request.data.get('adults')
        children = request.data.get('children')
        currency = request.data.get('currency', 'USD')

        if (check_in_date or check_out_date) is None:
            return Response({"error": "Check-in and check-out dates are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            hotel = Hotel.objects.get(id=hotel_id)
            room = Room.objects.get(id=room_id)

            # Check room availability for the specified dates
            if not is_room_available(room, check_in_date, check_out_date):
                return Response({"error": "Room not available for the specified dates."},
                                status=status.HTTP_400_BAD_REQUEST)

            hotel_currency = hotel.city.country.currency
            exchange_rate = 1
            if currency != hotel_currency:
                exchange_rate = get_exchange_rate(API_KEY_EXCHANGE_CURRENCY, hotel_currency, currency)
                if exchange_rate is None:
                    return Response({"error": "Failed to retrieve exchange rate."},
                                    status=status.HTTP_400_BAD_REQUEST)

            price = calculate_total_cost(check_in_date, check_out_date, room.price, exchange_rate)

            booking = Booking.objects.create(
                user=user,
                room=room,
                hotel=hotel,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                adults=adults,
                children=children,
                total_price=price
            )

            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except (Hotel.DoesNotExist, Room.DoesNotExist):
            return Response({"error": "Hotel or room not found."},
                            status=status.HTTP_400_BAD_REQUEST)


make_booking_view = MakeBooking.as_view()
