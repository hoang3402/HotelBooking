from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_create_view = UserCreateViewSet.as_view()


class UserLoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': user_serializer.data})


user_login_view = UserLoginAPIView.as_view()


class TestViewAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "detail": "Valid token."
        })


test_token = TestViewAPI.as_view()
