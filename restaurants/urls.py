from django.urls import path
from . import views


urlpatterns = [
    path('restaurants/', views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', views.RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),
]
