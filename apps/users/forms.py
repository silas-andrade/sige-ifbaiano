from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from apps.users.models import User
from django import forms

class UserFormRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'matricula', 'password1', 'password2', 'email')
        labels = {
            'full_name':'Nome completo',
            'matricula':'Matrícula',
            'email':'E-mail'
        }
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'matricula':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }