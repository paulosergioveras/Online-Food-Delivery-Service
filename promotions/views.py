from rest_framework import generics
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionListCreateView(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer