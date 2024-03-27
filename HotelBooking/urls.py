from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.http import HttpResponse

schema_view = get_schema_view(
    openapi.Info(
        title="Booking Hotel API",
        default_version='v1',
        description="Tma Intern",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nvh.02021995@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

def hello_world(request):
    return HttpResponse('Hello World')

urlpatterns = [
    path('', hello_world),
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls'), name='api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
