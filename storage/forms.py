from django.forms import ModelForm
from django import forms
from storage.models import Order

class RequestOrderForm(ModelForm):
    class Meta:
        model = Order
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