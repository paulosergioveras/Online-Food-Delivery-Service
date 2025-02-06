from reviews.models import Reviews
from orders.models import Order
from payments.models import Payment
from .models import Restaurant, Menu
from rest_framework import viewsets, generics, serializers
from .serializers import RestaurantSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


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
    






"""class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        restaurant = self.get_object()

        total_orders = Order.objects.filter(restaurant=restaurant).count()

        average_rating = Reviews.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))['rating__avg']

        popular_dishes = Menu.objects.filter(restaurant=restaurant).annotate(
            order_count=Count('orderitem')
        ).order_by('-order_count')[:5]

        revenue = Payment.objects.filter(order__restaurant=restaurant, status='SUCCESS').aggregate(
            total_revenue=models.Sum('amount')
        )['total_revenue'] or 0

        return Response({
            'total_orders': total_orders,
            'average_rating': average_rating,
            'popular_dishes': MenuSerializer(popular_dishes, many=True).data,
            'revenue': revenue,
        })"""


