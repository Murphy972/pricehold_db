from django.urls import path

from . import views

urlpatterns = [

    path('main/<str:pk>/', views.home, name='home'),
    path('pickup', views.by_pickup, name='pickup_date'),
    path('type-ph', views.by_ph, name='by_ph'),
    path('type-layaway', views.by_layaway, name='by_layaway'),
    path('truck-serta', views.truck_serta, name='truck_serta'),
    path('truck-sealy', views.truck_sealy, name='truck_sealy'),
    path('truck-united', views.truck_united, name='truck_united'),
    path('truck-ashley', views.truck_ashley, name='truck_ashley'),
    path('truck-freight', views.truck_freight, name='truck_freight'),
    path('order-view/<str:pk>/', views.order_view, name='order_view'),

]
