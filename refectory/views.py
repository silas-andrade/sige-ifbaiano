from django.shortcuts import render, redirect

def refectory_page(request):
    return render(request, 'refectory/refectory.html')
