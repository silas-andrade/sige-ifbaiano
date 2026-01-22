from django.urls import path

from .views import refectory_page

urlpatterns = [
    path('refectory/', refectory_page, name='refectory'),

]
