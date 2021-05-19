from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order
from .forms import *
from django.db.models import Q


def edit_orders(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    return render(request, 'createorder.html', {'form': form})


def home(request, *args, **kwargs):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    return render(request, 'home.html', {'order_date': order_date})


def by_pickup(request):
    orders = Order.objects.filter(order_isreserved=False)
    pickup_date = orders.order_by('pickup_date')
    return render(request, 'pickup_date.html', {'pickup_date': pickup_date})


def by_ph(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    ph_orders = order_date.filter(order_type='ph')
    return render(request, 'by_ph.html', {'ph_orders': ph_orders})


def by_layaway(request):
    orders = Order.objects.filter(order_isreserved=False)
    pickup_date = orders.order_by('pickup_date')
    layaway_orders = pickup_date.filter(order_type='layaway')
    return render(request, 'by_layaway.html', {'layaway_orders': layaway_orders})


def truck_serta(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    truck_serta = order_date.filter(truck='serta')
    return render(request, 'serta.html', {'truck_serta': truck_serta})


def truck_sealy(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    truck_sealy = order_date.filter(truck='sealy')
    return render(request, 'sealy.html', {'truck_sealy': truck_sealy})


def truck_united(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    truck_united = order_date.filter(truck='united')
    return render(request, 'united.html', {'truck_united': truck_united})


def truck_ashley(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    truck_ashley = order_date.filter(truck='ashley')
    return render(request, 'ashley.html', {'truck_ashley': truck_ashley})


def truck_freight(request):
    orders = Order.objects.filter(order_isreserved=False)
    order_date = orders.order_by('order_date')
    truck_freight = order_date.filter(truck='freight')
    return render(request, 'freight.html', {'truck_freight': truck_freight})


def order_view(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'order_view.html', context)

