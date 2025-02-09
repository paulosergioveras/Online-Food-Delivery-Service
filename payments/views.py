from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import stripe
from .models import Payment
from .serializers import PaymentSerializer


stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CreatePaymentIntentAPIView(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        total_price = request.data.get('total_price')

        if not order_id or not total_price:
            return Response(
                {'error': 'order_id and total_price are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            intent = stripe.PaymentIntent.create(
                amount=int(float(total_price) * 100),
                currency='usd',
                metadata={'order_id': order_id},
            )
            return Response({'client_secret': intent.client_secret})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)