from django.db import models
from django.forms import ModelForm
from datetime import datetime


class Order(models.Model):
    customer = models.CharField(max_length=20, blank=True)
    items = models.CharField(max_length=100, blank=True)
    order_date = models.DateTimeField(blank=True)
    pickup_date = models.DateField(blank=True)
    truck_options = [
        ('united', "United"),
        ('ashley', "Ashley"),
        ('serta', "Serta"),
        ('sealy', "Sealy"),
        ('freight', "Freight"),
    ]
    truck = models.CharField(
        max_length=100,
        choices=truck_options,
        blank=True
    )
    order_types = [
        ("ph", "PH"),
        ("layaway", "Layaway")
    ]
    order_type = models.CharField(
        max_length=100,
        choices=order_types,
        blank=True
    )
<<<<<<< HEAD
    order_isreserved = models.BooleanField(default=False, blank=True, null=True)
=======
    order_isreserved = models.BooleanField(default=False, blank=True)
    order_ismarked = models.BooleanField(default=False, blank=True)
>>>>>>> development

    def sort_by_od(self):
        return self

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Order, self).save(*args, **kwargs)

    def order_date_pretty(self):
        return self.order_date.strftime('%x %H:%M')

    def pickup_date_pretty(self):
        return self.pickup_date.strftime('%x')

    def __str__(self):
        return self.customer

    def id(self):
        return self.id
