from django.db import models

class Amenities(models.Model):
    amenity = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.amenity

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=256)
    hotel_price = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    updated_At  = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    updated_At  = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.hotel.hotel_name