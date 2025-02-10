from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from restaurants.serializers import RestaurantSerializer
from restaurants.models import Restaurant
from reviews.models import Reviews


class RestaurantListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantStatusView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Restaurant.objects.all()

    def get(self, request):
        total_restaurants = self.queryset.count()
        total_reviews = Reviews.objects.count()
        average_rating = Reviews.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']

    
        return response.Response(
            data = {
                'total_movies': total_restaurants,
                'total_reviews': total_reviews,
                'average_rating': round(average_rating, 1) if average_rating else 0,
            },
            status=status.HTTP_200_OK,
        )


