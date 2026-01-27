from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import Max
from django.utils import timezone

from .models import Token

@login_required(login_url='/accounts/login/')
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


@require_POST
@login_required
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


@require_POST
@login_required(login_url='/accounts/login/')
def validate_token(request, pk):
    if not request.user.is_staff:
        redirect('home')
    else:
        token = Token.objects.filter(id=pk)
        token.update(
            is_used = True
        )
        return redirect('refectory:home')