from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from menu.models import Menu
from menu.serializers import MenuSerializer
from restaurants.models import Restaurant


class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(owner=self.request.user)
        serializer.save(restaurant=restaurant)

    
class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
