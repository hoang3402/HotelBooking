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
from django.urls import include, path

from . import views

urlpatterns = [
    path('auth/', include('polls.auth.urls'), name='auth'),

    path('hotel/', views.hotel_list_view, name='hotels'),
    path('hotel/create/', views.hotel_create_view, name='create_hotel'),
    path('hotel/<int:pk>/', views.hotel_detail_view, name='detail_hotel'),
    path('hotel/<int:pk>/edit/', views.hotel_edit_view, name='edit_hotel'),
    path('hotel/<int:pk>/delete/', views.hotel_delete_view, name='delete_hotel'),

    path('room/', views.room_list_view, name='rooms'),
    path('room/create/', views.room_create_view, name='create_room'),
    path('room/<int:pk>/', views.room_detail_view, name='detail_room'),
    path('room/<int:pk>/edit/', views.room_edit_view, name='edit_room'),
    path('room/<int:pk>/delete/', views.room_delete_view, name='delete_room'),

    path('room-type/', views.room_type_list_view, name='room_type_list_view'),
    path('room-type/create/', views.room_type_create_view, name='room_type_create_view'),
    path('room-type/<str:pk>/edit/', views.room_type_edit_view, name='room_type_create_view'),
    path('room-type/<str:pk>/delete/', views.room_type_delete_view, name='room_type_create_view'),

    path('city/', views.city_list_view, name='city_list_view'),
    path('city/create/', views.city_create_view, name='city_create_view'),
    path('city/<str:pk>/edit/', views.city_edit_view, name='city_create_view'),
    path('city/<str:pk>/delete/', views.city_delete_view, name='city_create_view'),

    path('country/', views.country_list_view, name='country_list_view'),
    path('country/create/', views.country_create_view, name='country_create_view'),
    path('country/<str:pk>/edit/', views.country_edit_view, name='country_create_view'),
    path('country/<str:pk>/delete/', views.country_delete_view, name='country_create_view'),
]
