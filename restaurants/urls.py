from django.urls import path
from . import views


urlpatterns = [
    path('restaurants/', views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', views.RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),

    path('menus/', views.MenuListCreateView.as_view(), name='menus-list-create'),
    path('menus/<int:pk>/', views.MenuRetrieveUpdateDestroyView.as_view(), name='menus-detail'),
]
