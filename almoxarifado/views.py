from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import User
from almoxarifado.models import (
    Order, OrderItem, Item
    )

@login_required(login_url='accounts/login/')
def request_order_page(request):
    items = Item.objects.filter(quantity_available__gt=0)

    context = {
        "items": items
    }

    return render(request, 'almoxarifado/requestorder.html', context)

    
import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required(login_url='accounts/login/')
@require_POST
def RequestOrder(request):
    try:
        data = json.loads(request.body)
        items = data.get('items', [])

        if not items:
            return JsonResponse({'message': 'Carrinho vazio.'}, status=400)

        order = Order.objects.create(user=request.user)

        for item in items:
            item_id = item.get('id')
            quantity = int(item.get('quantity', 0))

            if quantity <= 0:
                continue

            product = Item.objects.get(id=item_id)

            if quantity > product.quantity_available:
                return JsonResponse({
                    'message': f'Estoque insuficiente para {product.name}'
                }, status=400)

            OrderItem.objects.create(
                order=order,
                item=product,
                quantity=quantity,
                is_returnable=True
            )

            # Atualiza estoque
            product.quantity_available -= quantity
            product.save()

        return JsonResponse({'message': 'Pedido realizado com sucesso'}, status=200)

    except Item.DoesNotExist:
        return JsonResponse({'message': 'Item não encontrado.'}, status=404)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
