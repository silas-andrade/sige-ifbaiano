from django.urls import path

from .views import almocar_page

urlpatterns = [
    path('home/', almocar_page, name='almocar'),
]
