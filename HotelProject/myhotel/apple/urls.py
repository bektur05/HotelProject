from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'room', RoomViewSet, basename='room_list')
router.register(r'users', UserProfileViewSet, basename='users_list')
router.register(r'review', ReviewViewSet, basename='review_list')

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('city/', CityListAPIViewSet.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_list'),
]