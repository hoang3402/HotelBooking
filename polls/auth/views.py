from django.contrib.auth import authenticate, login
from rest_framework import generics, response, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from polls.auth.serializers import UserSerializer, get_tokens_for_user
from polls.models import User


class StaffPermission(BasePermission):
    message = 'Only staff members can access this endpoint.'

    def has_permission(self, request, view):
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class AdminPermission(BasePermission):
    message = 'Only Admin can access this endpoint.'

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class UserCreateViewSet(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super(UserCreateViewSet, self).create(request, *args, **kwargs)
        user_data = response.data
        user = User.objects.get(pk=user_data['id'])
        token = get_tokens_for_user(user)

        return Response({
            'refresh': token['refresh'],
            'access': token['access'],
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
            token = get_tokens_for_user(user)

            response_data = {
                'refresh': token['refresh'],
                'access': token['access'],
                'user': UserSerializer(user).data,
            }

            return response.Response(response_data, status=status.HTTP_200_OK)

        except AuthenticationFailed as e:
            return response.Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception:
            return response.Response({'error': 'An internal error occurred.'},
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)


user_login_view = UserLoginViewSet.as_view()


class RefreshTokenViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            refresh = RefreshToken(request.data.get('refresh'))

            return response.Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        except Exception:
            return response.Response({'error': 'An internal error occurred.'},
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)


refresh_token_view = RefreshTokenViewSet.as_view()


class TestViewAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "detail": "Valid token."
        })


test_token = TestViewAPI.as_view()


class PermissionsViewAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermission]

    def post(self, request, user_id):
        if not user_id:
            return Response({'error': 'User ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.is_staff = True
        user.save()

        return Response({'detail': 'success'}, status=status.HTTP_200_OK)


permissions = PermissionsViewAPI.as_view()


class CheckPermissionAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser is True:
            return Response({'detail': 'You are an admin.'}, status=status.HTTP_200_OK)

        if user.is_staff is True:
            return Response({'detail': 'You are a staff member.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'You are customer.'}, status=status.HTTP_403_FORBIDDEN)


check_permission = CheckPermissionAPI.as_view()


class LogoutAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


user_logout_view = LogoutAPI.as_view()
