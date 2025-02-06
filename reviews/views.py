from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework import generics
from restaurants.models import Restaurant
from rest_framework.permissions import IsAuthenticated


class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client = self.request.user
        restaurant_id = self.request.data.get('restaurant_id')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer.save(client=client, restaurant=restaurant)


class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

