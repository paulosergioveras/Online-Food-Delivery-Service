from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Avg


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    stripe.api_key = settings.STRIPE_SECRET_KEY

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