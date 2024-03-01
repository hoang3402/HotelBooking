from django.contrib import admin

from polls.models import Booking, Hotel, Review, Room, User, RoomType, SpecificHotelFeature, HotelFeatures, Country, \
    City

admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(RoomType)
admin.site.register(SpecificHotelFeature)
admin.site.register(HotelFeatures)
admin.site.register(Country)
admin.site.register(City)
