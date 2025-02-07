from django.urls import path, include
from django.contrib import admin

from restaurants.views import (
    RestaurantListCreateView,
    RestaurantRetrieveUpdateDestroyView,
    MenuListCreateView,
    MenuRetrieveUpdateDestroyView
    )

from reviews.views import ReviewsListCreateView, ReviewsRetrieveUpdateDestroyView
from support.views import SupportTicketListCreateView, SupportTicketRetrieveUpdateDestroyView

from orders.views import OrderListCreateView, OrderRetrieveUpdateDestroyView
    
    


urlpatterns = [
    path('admin/', admin.site.urls),

    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),

    path('menus/', MenuListCreateView.as_view(), name='menus-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyView.as_view(), name='menus-detail'),

    path('reviews/', ReviewsListCreateView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyView.as_view(), name='reviews-detail'),

    path('support/', SupportTicketListCreateView.as_view(), name='support-list-create'),
    path('support/<int:pk>/', SupportTicketRetrieveUpdateDestroyView.as_view(), name='support-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]