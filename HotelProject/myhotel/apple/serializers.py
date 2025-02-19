from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_images']


class CitySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']



class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'



class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'comment', 'stars']



class HotelListSerializers(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(many=True, read_only=True)
    city = CitySimpleSerializers()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_image', 'city', 'description', 'street',
                  'owner']



class HotelDetailSerializers(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(many=True, read_only=True)
    city = CitySimpleSerializers()
    owner = UserProfileSimpleSerializers()
    reviews = ReviewSerializers(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_image', 'city', 'country', 'hotel_stars', 'description', 'street', 'owner', 'reviews']
        owner = UserProfileSimpleSerializers()



class CityDetailSerializers(serializers.ModelSerializer):
    city_hotels = HotelListSerializers(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_images', 'city_hotels']
