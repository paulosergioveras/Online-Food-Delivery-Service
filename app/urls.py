from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('restaurants.urls')),
    path('api/vi/', include('menu.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('support.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('promotions.urls')),
    path('api/v1/', include('payments.urls'))
]
