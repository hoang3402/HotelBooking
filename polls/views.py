from rest_framework import viewsets

from polls.models import City, Country
from polls.serializers import CitySerializer, CountrySerializer


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
