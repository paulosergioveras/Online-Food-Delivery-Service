from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewsListCreateView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', views.ReviewsRetrieveUpdateDestroyView.as_view(), name='reviews-detail'),
]
