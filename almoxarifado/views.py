from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from almoxarifado.models import Order, OrderItem, Item


@login_required(login_url='accounts/login/')
def RequestOrder(request):
    if request.method == "POST":
        items_request = request.POST.getlist("items[]")

        if not items_request:
            messages.error(request, "Selecione pelo menos um item.")
            return redirect("request-order")

        # cria o pedido
        order = Order.objects.create(user=request.user)

        for item in items_request:
            item_id, quantity = item.split(":")
            quantity = int(quantity)

            item_obj = Item.objects.get(id=item_id)
            item_obj.quantity_available -= quantity
            if quantity > item_obj.quantity_available:
                messages.error(
                    request,
                    f"Estoque insuficiente para {item_obj.name}"
                )
                order.delete()
                return redirect("request-order")

            OrderItem.objects.create(
                order=order,
                item=item_obj,
                quantity=quantity
            )
        
        messages.success(request, "Pedido realizado com sucesso!")
        #return redirect("order-history")
        return redirect("home")
    context = {
        'items': Item.objects.filter(quantity_available__gt=0)
    }
    return render(request, 'almoxarifado/requestorder.html', context)


# =========================
# HISTÓRICO DO ALUNO
# =========================
@login_required(login_url='accounts/login/')
def order_history(request):
   pass
   """ orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'almoxarifado/order_history.html', {
        'orders': orders
    })
"""

# =========================
# ÁREA DO ALMOXARIFE
# =========================
@staff_member_required
def manage_orders(request):
    orders = Order.objects.filter(is_approved=False)
    return render(request, 'almoxarifado/manage_orders.html', {
        'orders': orders
    })


@staff_member_required
def approve_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if order.is_approved:
        return redirect('manage-orders')

    for order_item in order.orderitem_set.all():
        item = order_item.item
        item.quantity_available -= order_item.quantity
        item.save()

    order.is_approved = True
    order.save()

    messages.success(request, "Pedido aprovado com sucesso!")
    return redirect('manage-orders')


@staff_member_required
def reject_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()

    messages.success(request, "Pedido rejeitado.")
    return redirect('manage-orders')
