from django.shortcuts import render, redirect

# Create your views here.
def almocar_page(request):
    return redirect('home')

def refeitorio_page(request):
    return render(request, 'almocar/refeitorio.html')
