from django.shortcuts import render, redirect
from delivery.models import Restaurant, Menu, Order, OrderItem, Reviews, Promotion, Payment, SupportTicket
from rest_framework import viewsets
from delivery.serializers import (
    RestaurantSerializer, 
    MenuSerializer, 
    OrderSerializer, 
    OrderItemSerializer, 
    ReviewsSerializer, 
    PromotionSerializer, 
    PaymentSerializer,
    SupportTicketSerializer )
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Avg

class RestaurantViewSet(viewsets.ModelViewSet):
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
        })

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['post'])
    def create_payment_intent(self, request):
        order_id = request.data.get('order_id')
        total_price = request.data.get('total_price')
        try:
            intent = stripe.PaymentIntent.create(
                total_price=total_price,
                currency='usd',
                metadata={'order_id': order_id},
            )
            return Response({'client_secret': intent.client_secret})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer




