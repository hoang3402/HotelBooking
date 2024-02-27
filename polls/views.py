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
