from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from restaurants.models import Restaurant


class ReviewsListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def perform_create(self, serializer):
        client = self.request.user
        restaurant_id = self.request.data.get('restaurant_id')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer.save(client=client, restaurant=restaurant)


class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

