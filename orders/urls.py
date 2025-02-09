from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]
