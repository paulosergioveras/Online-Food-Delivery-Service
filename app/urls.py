from django.urls import path, include
from django.contrib import admin
from restaurants.views import (
    RestaurantListCreateView, RestaurantRetrieveUpdateDestroyView, MenuListCreateView,
    MenuRetrieveUpdateDestroyView)
from reviews.views import ReviewsListCreateView, ReviewsRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),

    path('menus/', MenuListCreateView.as_view(), name='menus-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyView.as_view(), name='menus-detail'),

    path('reviews/', ReviewsListCreateView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>', ReviewsRetrieveUpdateDestroyView.as_view(), name='reviews-detail')
]