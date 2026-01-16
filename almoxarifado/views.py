from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import User


@login_required(login_url='accounts/login/')
def RequestOrder(request):
    context = {
        "user":User.objects.get(full_name=request.user.full_name),
        
    }
    return render(request, 'almoxarifado/requestorder.html', context)