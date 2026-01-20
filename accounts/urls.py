from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import LoginPage, RegisterPage, LogoutUser, ProfilePage


urlpatterns = [
    
    path('register/', RegisterPage, name='register'),
    path('logout/', LogoutUser, name='logout'),
    path('login/', LoginPage, name='login'),
    path('profile/', ProfilePage, name='profile'),

]

