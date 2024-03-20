from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from polls.auth.serializers import UserSerializer, get_tokens_for_user, AdminPermission
from polls.auth.swagger import *
from polls.models import User


class UserCreateViewSet(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=user_register_params, responses={200: response_auth})
    def post(self, request, *args, **kwargs):
        request.data['is_staff'] = False
        request.data['is_superuser'] = False
        user_data = User.objects.create(**request.data)
        token = get_tokens_for_user(user_data)

        return Response({
            'refresh': token['refresh'],
            'access': token['access'],
            'user': UserSerializer(user_data).data
        })


user_create_view = UserCreateViewSet.as_view()


class UserLoginViewSet(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=user_login_params, responses={200: response_auth})
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

    @swagger_auto_schema(request_body=refresh_token, responses={200: response_refresh})
    def post(self, request, *args, **kwargs):
        try:
            refresh = RefreshToken(request.data.get('refresh'))

            return response.Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        except Exception as e:
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]

    def create(self, request, *args, **kwargs):

        role = request.data.get('role')

        if role not in ['user', 'staff', 'admin']:
            return Response({'detail': 'role must be user, staff or admin'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        role = request.data.get('role')

        if role not in ['user', 'staff', 'admin']:
            return Response({'detail': 'role must be user, staff or admin'}, status=status.HTTP_400_BAD_REQUEST)

        match role:
            case 'user':
                user.is_staff = False
                user.is_superuser = False
            case 'staff':
                user.is_staff = True
                user.is_superuser = False
            case 'admin':
                user.is_staff = True
                user.is_superuser = True

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


users = UserViewSet.as_view({'get': 'list'})
get_user = UserViewSet.as_view({'get': 'retrieve'})
create_user = UserViewSet.as_view({'post': 'create'})
edit_user = UserViewSet.as_view({'patch': 'partial_update'})
delete_user = UserViewSet.as_view({'delete': 'destroy'})
