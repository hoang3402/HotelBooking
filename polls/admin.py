from django.contrib import admin

from polls.models import Booking, Hotel, Review, Room, User, RoomType, SpecificHotelFeature, HotelFeatures, Country, \
    City


@admin.register(Booking)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecificHotelFeature)
class HotelFeaturesAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelFeatures)
class HotelFeaturesAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
