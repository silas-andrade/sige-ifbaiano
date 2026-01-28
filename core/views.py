from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'core/home.html')


@login_required(login_url="/accounts/login/")
def about(request):
    return render(request, 'core/about.html')


