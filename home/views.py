from django.shortcuts import render

from .models import Order


def home(request):
    orders = Order.objects
    return render(request, 'home.html', {'orders': orders})

