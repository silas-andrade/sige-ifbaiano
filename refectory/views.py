from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .models import Token

@login_required(login_url='/accounts/login/')
def refectory_page(request):
    user = request.user
    token = Token.objects.filter()
    context = {
        'user':user
    }
    return render(request, 'refectory/refectory.html', context)


@login_required(login_url='/accounts/login/')
def create_token(request):
    user = request.user
    token = Token.objects.create(
        user=user,
        )
    return redirect('refectory')    


@login_required(login_url='/accounts/login/')
def validate_token(request):
    if request.method == 'POST':
        pass