from django
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_isreserved', 'order_ismarked']
