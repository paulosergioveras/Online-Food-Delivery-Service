from django.urls import path
from . import views


urlpatterns = [
    path('menus/', views.MenuListCreateView.as_view(), name='menus-list-create'),
    path('menus/<int:pk>/', views.MenuRetrieveUpdateDestroyView.as_view(), name='menus-detail'),
]
