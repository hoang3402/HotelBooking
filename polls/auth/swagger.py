from drf_yasg import openapi

user_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User Email'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
        'number_phone': openapi.Schema(type=openapi.TYPE_STRING, description='Number Phone'),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Active'),
        'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role')
    }
)

user_login_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user')
    },
    required=['email', 'password']
)

user_register_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
        'number_phone': openapi.Schema(type=openapi.TYPE_STRING, description='Number Phone'),
    }
)

response_auth = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
        'user': user_response
    }
)

refresh_token = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
    }
)

response_refresh = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
    }
)
