import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Token

@login_required(login_url='/accounts/login/')
def refectory_page(request):
    context = {
    }
    return render(request, 'refectory/refectory.html', context)



def create_token(request):
    user = request.user
    token = Token.objects.create(
        user=user,
        )
    return redirect('refectory')    