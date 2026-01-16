from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import RequestOrder, request_order_page


urlpatterns = [
    
    path('request-order-api/', RequestOrder, name='request-order-api'),
    path('request-order/', request_order_page, name='request-order'),
]

