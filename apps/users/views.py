from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserFormRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# Create your views here.

def RegisterPage(request):
    form = UserFormRegister()

    if request.method == 'POST':
        form = UserFormRegister(request.POST)
        
        if form.is_valid():

            user = form.save(commit=False)
            user.matricula = user.matricula.upper()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ocorreu um erro durante o registro!')


    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)


def LoginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')

    return render(request, "users/login.html")


@login_required(login_url='/accounts/login/')
def LogoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/accounts/login/')
def ProfilePage(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'users/profile.html', context)

def RecoverPassword(request):
    pass

def person_list(request):
    # Retrieve all person objects from the database
    #people = Person.objects.all()
    #context = {
    #    "people": people
    #}
    # Pass the data to the template
    #return render(request, 'person_list.html', context)
    pass