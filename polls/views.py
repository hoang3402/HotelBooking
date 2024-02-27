from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from polls.models import Hotel, User
from polls.serializers import HotelSerializer, UserSerializer


class HotelViewSet(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_list_view = HotelViewSet.as_view()


class HotelDetailViewSet(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_detail_view = HotelDetailViewSet.as_view()


class HotelCreateViewSet(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_create_view = HotelCreateViewSet.as_view()


class HotelEditViewSet(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_edit_view = HotelEditViewSet.as_view()


class HotelDeleteViewSet(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


hotel_delete_view = HotelDeleteViewSet.as_view()


class UserCreateViewSet(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    queryset = User.objects.all()
    serializer_class = UserSerializer


user_create_view = UserCreateViewSet.as_view()
