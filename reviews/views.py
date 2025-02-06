from .models import Reviews
from rest_framework import viewsets
from .serializers import ReviewsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
