from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer