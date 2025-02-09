from django.urls import path
from . import views


urlpatterns = [
    path('promotions/', views.PromotionListCreateView.as_view(), name='promotions-list-create'),
    path('promotions/<int:pk>/', views.PromotionRetrieveUpdateDestroyView.as_view(), name='promotions-detail'),
]
