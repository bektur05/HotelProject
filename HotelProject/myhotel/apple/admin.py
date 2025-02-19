from django.contrib import admin
from .models import *
#from modeltranslation.admin import TranslationAdmin


admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Booking)
admin.site.register(Review)


