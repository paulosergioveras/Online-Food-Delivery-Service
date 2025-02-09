from django.urls import path
from . import views


urlpatterns = [
    path('support/', views.SupportTicketListCreateView.as_view(), name='support-list-create'),
    path('support/<int:pk>/', views.SupportTicketRetrieveUpdateDestroyView.as_view(), name='support-detail'),
]
