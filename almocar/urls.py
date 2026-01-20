from django.urls import path

from .views import almocar_page, refeitorio_page

urlpatterns = [
    path('refeitorio/', refeitorio_page, name='almocar'),
    path('refeitorio/', almocar_page, name='refeitorio'),

]
