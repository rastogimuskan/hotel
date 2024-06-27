from django.contrib import admin
from main import models

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'hotel_price', 'description']


admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Amenities)
admin.site.register(models.HotelImage)