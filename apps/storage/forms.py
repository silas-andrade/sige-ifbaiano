from django.forms import ModelForm
from django import forms
from apps.storage.models import Order

class RequestOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'enrollment_number', 'password1', 'password2', 'email')
        labels = {
            'full_name':'Nome completo',
            'enrollment_number':'Matrícula',
            'email':'E-mail'
        }
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment_number':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }