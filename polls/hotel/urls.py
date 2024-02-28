"""
URL configuration for HotelBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotel_list_view, name='hotels'),
    path('create/', views.hotel_create_view, name='create_hotel'),
    path('<int:pk>/', views.hotel_detail_view, name='detail_hotel'),
    path('<int:pk>/edit/', views.hotel_edit_view, name='edit_hotel'),
    path('<int:pk>/delete/', views.hotel_delete_view, name='delete_hotel'),
]
