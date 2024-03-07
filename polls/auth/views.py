from django.contrib.auth import authenticate, login
from rest_framework import generics, response, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from polls.auth.serializers import UserSerializer
from polls.models import User


class UserCreateViewSet(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super(UserCreateViewSet, self).create(request, *args, **kwargs)
        user_data = response.data
        user = User.objects.get(pk=user_data['id'])
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_data
        })


user_create_view = UserCreateViewSet.as_view()


class UserLoginViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('email')
            password = request.data.get('password')

            if not username or not password:
                raise AuthenticationFailed('Both username and password are required.')

            user = authenticate(username=username, password=password)

            if not user:
                raise AuthenticationFailed('Invalid username or password.')

            login(request, user)
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
            }

            return response.Response(response_data, status=status.HTTP_200_OK)

        except AuthenticationFailed as e:
            return response.Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            # Handle unexpected errors gracefully (e.g., log the error and return a generic error message)
            return response.Response({'error': 'An internal error occurred.'},
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)


user_login_view = UserLoginViewSet.as_view()


class TestViewAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "detail": "Valid token."
        })


test_token = TestViewAPI.as_view()
