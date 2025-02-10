from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer