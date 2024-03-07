from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from HotelBooking.settings import API_KEY_EXCHANGE_CURRENCY
from polls.auth.views import StaffPermission, AdminPermission
from polls.serializers import *
from polls.utilities import calculate_total_cost, get_exchange_rate, days_available, is_room_available


# Hotel

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


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
    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


staff_room_list_view = RoomViewSet.as_view({'get': 'list'})
staff_room_detail_view = RoomViewSet.as_view({'get': 'retrieve'})
staff_room_create_view = RoomViewSet.as_view({'post': 'create'})
staff_room_edit_view = RoomViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
staff_room_delete_view = RoomViewSet.as_view({'delete': 'destroy'})


# RoomType

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


room_type_list_view = RoomTypeViewSet.as_view({'get': 'list'})
room_type_create_view = RoomTypeViewSet.as_view({'post': 'create'})
room_type_edit_view = RoomTypeViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
room_type_delete_view = RoomTypeViewSet.as_view({'delete': 'destroy'})


# Feature

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = HotelFeatures.objects.all()
    serializer_class = FeatureSerializer
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


feature_list_view = FeatureViewSet.as_view({'get': 'list'})
feature_create_view = FeatureViewSet.as_view({'post': 'create'})
feature_edit_view = FeatureViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
feature_delete_view = FeatureViewSet.as_view({'delete': 'destroy'})


# Feature hotel

class FeatureHotelViewSet(viewsets.ModelViewSet):
    queryset = SpecificHotelFeature.objects.all()
    serializer_class = SpecificHotelFeatureSerializer
    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [StaffPermission, AdminPermission],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }

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
    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [StaffPermission, AdminPermission],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


city_list_view = CityViewSet.as_view({'get': 'list'})
city_create_view = CityViewSet.as_view({'post': 'create'})
city_edit_view = CityViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
city_delete_view = CityViewSet.as_view({'delete': 'destroy'})


# Country

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [StaffPermission, AdminPermission],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


country_list_view = CountryViewSet.as_view({'get': 'list'})
country_create_view = CountryViewSet.as_view({'post': 'create'})
country_edit_view = CountryViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
country_delete_view = CountryViewSet.as_view({'delete': 'destroy'})


# Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes_by_action = {
        'list': [StaffPermission, AdminPermission],
        'retrieve': [StaffPermission, AdminPermission],
        'create': [StaffPermission, AdminPermission],
        'update': [StaffPermission, AdminPermission],
        'partial_update': [StaffPermission, AdminPermission],
        'destroy': [AdminPermission]
    }


staff_booking_list_view = BookingViewSet.as_view({'get': 'list'})
staff_booking_detail_view = BookingViewSet.as_view({'get': 'retrieve'})
staff_booking_create_view = BookingViewSet.as_view({'post': 'create'})
staff_booking_edit_view = BookingViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
staff_booking_delete_view = BookingViewSet.as_view({'delete': 'destroy'})


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


class ViewBookings(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


view_bookings_view = ViewBookings.as_view()


class MakeBooking(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        room_id = request.data.get('room_id')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')
        currency = request.data.get('currency', 'USD')

        if (check_in_date or check_out_date) is None:
            return Response({"error": "Check-in and check-out dates are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            room = Room.objects.get(id=room_id)

            if room.is_available is False:
                return Response({"error": "Room not available."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Check room availability for the specified dates
            if not is_room_available(room, check_in_date, check_out_date):
                return Response({"error": "Room not available for the specified dates."},
                                status=status.HTTP_400_BAD_REQUEST)

            hotel_currency = room.hotel.city.country.currency
            exchange_rate = 1
            if currency != hotel_currency:
                exchange_rate = get_exchange_rate(API_KEY_EXCHANGE_CURRENCY, hotel_currency, currency)
                if exchange_rate is None:
                    return Response({"error": "Failed to retrieve exchange rate."},
                                    status=status.HTTP_400_BAD_REQUEST)

            price = calculate_total_cost(check_in_date, check_out_date, room.price, exchange_rate)

            exchange_rate = 1
            if hotel_currency != 'USD':
                exchange_rate = get_exchange_rate(API_KEY_EXCHANGE_CURRENCY, hotel_currency, 'USD')
                if exchange_rate is None:
                    return Response({"error": "Failed to retrieve exchange rate."},
                                    status=status.HTTP_400_BAD_REQUEST)

            total_price_usd = calculate_total_cost(check_in_date, check_out_date, room.price, exchange_rate)

            booking = Booking.objects.create(
                user=user,
                room=room,
                hotel=room.hotel,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                total_price=price,
                currency=currency,
                total_price_usd=total_price_usd
            )

            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except (Hotel.DoesNotExist, Room.DoesNotExist):
            return Response({"error": "Hotel or room not found."},
                            status=status.HTTP_400_BAD_REQUEST)


make_booking_view = MakeBooking.as_view()


class ViewBooking(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk, user=request.user)
            serializer = BookingDetailsSerializer(booking)
            return Response(serializer.data)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)


view_booking_view = ViewBooking.as_view()


class CancelBooking(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk, user=request.user)

            if booking.status == 'Cancelled':
                return Response({"message": "Booking already canceled."}, status=status.HTTP_400_BAD_REQUEST)

            if booking.status == 'Completed':
                return Response({"message": "Booking already completed."}, status=status.HTTP_400_BAD_REQUEST)

            if booking.status == 'Confirmed':
                return Response({"message": "Booking already confirmed."}, status=status.HTTP_400_BAD_REQUEST)

            booking.status = 'Cancelled'
            booking.save()
            return Response({"message": "Booking canceled successfully."}, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)


cancel_booking_view = CancelBooking.as_view()


class DaysRoomAvailableBooking(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        room_id = request.data.get('room_id')
        year = request.data.get('year')
        month = request.data.get('month')

        if (year or month) is None:
            return Response({"error": "Check-in and check-out dates are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        # try parameter
        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return Response({"error": "Invalid year or month."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            room = Room.objects.get(id=room_id)

            if room.is_available is False:
                return Response({"error": "Room not available."},
                                status=status.HTTP_400_BAD_REQUEST)

            is_available = days_available(room, year, month)
            return Response({"days": is_available}, status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)


days_room_available_view = DaysRoomAvailableBooking.as_view()


class ToggleRoomAvailability(APIView):
    permission_classes = [StaffPermission, AdminPermission]

    def post(self, request, pk):
        try:
            room = Room.objects.get(id=pk)
            room.is_available = not room.is_available
            room.save()
            return Response({"message": "Room availability toggled successfully."},
                            status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)


toggle_room_availability_view = ToggleRoomAvailability.as_view()
