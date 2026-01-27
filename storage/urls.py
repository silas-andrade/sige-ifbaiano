from django.urls import path

from .views import (
    RequestOrder,
    order_history,
    manage_orders,
    approve_order,
    reject_order,
)

app_name = 'storage'

urlpatterns = [

    path('request-order/', RequestOrder, name='request-order'),

    # Histórico do aluno
    path('order-history/', order_history, name='order-history'),

    # Almoxarife
    path('manage-orders/', manage_orders, name='manage-orders'),
    path('approve-order/<int:order_id>/', approve_order, name='approve-order'),
    path('reject-order/<int:order_id>/', reject_order, name='reject-order'),
]
