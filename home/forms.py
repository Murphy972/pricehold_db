
from django.forms import ModelForm
from .models import Order
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control order-view-param'}),
            'items': forms.TextInput(attrs={'class': 'form-control'}),
            'order_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'pickup_date': forms.TextInput(attrs={'class': 'form-control'}),
            'truck': forms.Select(attrs={'class': 'form-control'}),
            'order_type': forms.Select(attrs={'class': 'form-control'}),
            'order_isreserved': forms.CheckboxInput(),
        }
