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
    path('room-type/<str:pk>/edit/', views.room_type_edit_view, name='room_type_edit_view'),
    path('room-type/<str:pk>/delete/', views.room_type_delete_view, name='room_type_delete_view'),

    path('feature/', views.feature_list_view, name='feature_list_view'),
    path('feature/create/', views.feature_create_view, name='feature_create_view'),
    path('feature/<str:pk>/edit/', views.feature_edit_view, name='feature_edit_view'),
    path('feature/<str:pk>/delete/', views.feature_delete_view, name='feature_delete_view'),

    path('feature-hotel/', views.feature_hotel_list_view, name='feature_hotel_list_view'),
    path('feature-hotel/<int:pk>/', views.feature_hotel_detail_view, name='feature_hotel_list_view'),
    path('feature-hotel/create/', views.feature_hotel_create_view, name='feature_hotel_create_view'),
    path('feature-hotel/<str:pk>/edit/', views.feature_hotel_edit_view, name='feature_hotel_edit_view'),
    path('feature-hotel/<str:pk>/delete/', views.feature_hotel_delete_view, name='feature_hotel_delete_view'),

    path('city/', views.city_list_view, name='city_list_view'),
    path('city/create/', views.city_create_view, name='city_create_view'),
    path('city/<str:pk>/edit/', views.city_edit_view, name='city_edit_view'),
    path('city/<str:pk>/delete/', views.city_delete_view, name='city_delete_view'),

    path('country/', views.country_list_view, name='country_list_view'),
    path('country/create/', views.country_create_view, name='country_create_view'),
    path('country/<str:pk>/edit/', views.country_edit_view, name='country_edit_view'),
    path('country/<str:pk>/delete/', views.country_delete_view, name='country_delete_view'),

    path('staff/booking/', views.staff_booking_list_view, name='staff_booking_list_view'),
    path('staff/booking/<int:pk>/', views.staff_booking_detail_view, name='staff_booking_list_view'),
    path('staff/booking/create/', views.staff_booking_create_view, name='staff_booking_create_view'),
    path('staff/booking/<str:pk>/edit/', views.staff_booking_edit_view, name='staff_booking_edit_view'),
    path('staff/booking/<str:pk>/delete/', views.staff_booking_delete_view, name='staff_booking_delete_view'),

    path('booking/', views.view_bookings_view, name="booking_list_view"),
    path('booking/<int:pk>/', views.view_booking_view, name="booking_detail_view"),
    path('booking/create/', views.make_booking_view, name="make_booking"),
    path('booking/cancel/<int:pk>/', views.cancel_booking_view, name="cancel_booking"),

    path('search/', views.search_view, name="search"),
    path('is-available/', views.days_room_available_view, name="is_room_available"),
]
