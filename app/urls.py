from django.urls import path, include
from rest_framework.routers import DefaultRouter
from delivery.views import (
    RestaurantViewSet, 
    MenuViewSet, 
    OrderViewSet, 
    OrderItemViewSet, 
    ReviewsViewSet, 
    PromotionViewSet, 
    PaymentViewSet,
    SupportTicketViewSet )

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewsViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'support-tickets', SupportTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/create-payment-intent/', PaymentViewSet.as_view({'post': 'create_payment_intent'})),
]