from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.PaymentListCreateView.as_view(), name='payments-list-create'),
    path('payments/<int:pk>/', views.PaymentRetrieveUpdateDestroyView.as_view(), name='payments-detail'),
    path('payments/create_payment_intent/', views.CreatePaymentIntentAPIView.as_view(), name='payments-create_payment_intent'),
]
