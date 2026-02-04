from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction
from django.utils import timezone
from django.db.models import Max

from .models import Token

@login_required(login_url='/users/login/')
def refectory_page(request):
    today = timezone.now().date()
    user = request.user
    token = Token.objects.filter(
    user=user,
    created_at__date=today,
    is_valid=True
    ).first()
    context = {
        'user':user,
        'token':token,
    }
    return render(request, 'refectory/refectory.html', context)


@login_required(login_url='/users/login/')
def queue_status(request):
    """
    Retorna apenas o HTML do status da fila do usuário
    """
    user = request.user

    # Todos tokens válidos e não usados, ordenados pelo tempo de criação (fila)
    tokens = Token.objects.filter(is_used=False, is_valid=True).order_by('created_at')

    # Pega o token do usuário mais recente (ou o único) ainda não usado
    user_token = tokens.filter(user=user).first()

    if user_token:
        # Converte para lista para poder usar index()
        token_list = list(tokens)
        try:
            position = token_list.index(user_token) + 1  # posição na fila
        except ValueError:
            position = 0
        est_time = position * 5  # cada ficha leva 5 minutos
    else:
        position = 0
        est_time = 0

    context = {
        "position": position,
        "est_time": est_time
    }

    return render(request, "refectory/partials/queue_status.html", context)


@require_POST
@login_required(login_url='/users/login/')
@transaction.atomic
def create_token(request):
    user = request.user
    today = timezone.now().date()

    Token.objects.filter(
        user=user,
        created_at__date=today,
        is_valid=True
    ).update(
        is_valid=False,
        invalidated_reason="User requested a new token, replacing the previous one."
    )

    last_token = (
        Token.objects
        .filter(created_at__date=today)
        .aggregate(Max('token'))['token__max']
    )

    Token.objects.create(
        user=user,
        token=(last_token or 0) + 1
    )

    return redirect('refectory:home')

from django.db import transaction


@require_POST
@login_required(login_url='/users/login/')
def validate_token(request, pk):
    if not request.user.is_staff:
        return redirect('home')

    with transaction.atomic():
        token = Token.objects.select_for_update().get(id=pk)

        if token.is_used:
            return redirect('moderator:scanner')

        token.is_used = True
        token.used_at = timezone.now()
        token.save()

    return redirect('moderator:scanner')

@login_required(login_url='/users/login/')
def scan_token(request, pk):

    if not request.user.is_staff:
        return redirect('home')

    token = get_object_or_404(Token, id=pk)

    if token.is_used:
        return redirect('moderator:scanner')

    return render(
        request,
        "refectory/scan_token.html",
        {"token": token}
    )