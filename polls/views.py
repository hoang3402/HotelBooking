from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from polls.models import Hotel
from polls.serializers import HotelSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def index(request):
    data_query = Hotel.objects.all()
    serializer = HotelSerializer(data_query, many=True)
    return Response(serializer.data)
