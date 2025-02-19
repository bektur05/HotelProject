from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                        MaxValueValidator(80)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    data_registered = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('client', 'Client'),
        ('owner', 'Owner'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='client')
    user_country = models.CharField(max_length=64, null=True, blank=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class City(models.Model):
    city_name = models.CharField(max_length=32, unique=True)
    city_images = models.ImageField(upload_to='city_Image/')

    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_hotels')
    street = models.CharField(max_length=100)
    description = models.TextField()
    all_inclusive = models.BooleanField()
    hotel_stars = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1),
                                                        MaxValueValidator(5)],)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_image')
    hotel_image = models.ImageField(upload_to='hotel_image/')



class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_number = models.IntegerField()
    description = models.TextField()
    ROOM_CHOICES = (
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занять', 'занять')
    )
    room_status = models.CharField(max_length=64, choices=ROOM_CHOICES)
    TYPE_CHOICES = (
        ('Люкс', 'Люкс'),
        ('Семейный', 'Семейный'),
        ('Одноместный', 'Одноместный')
    )
    room_type = models.CharField(max_length=64, choices=ROOM_CHOICES)
    price = models.PositiveSmallIntegerField()


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )
    book_status = models.CharField(max_length=50, choices=STATUS_BOOK_CHOICES)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user}, {self.hotel}'



class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(10, 30)],
                                             null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'









