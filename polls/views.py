from rest_framework import generics

from polls.models import Hotel
from polls.serializers import HotelSerializer


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