from django.db import models
from django.forms import ModelForm


class Order(models.Model):
    customer = models.CharField(max_length=20)
    items = models.CharField(max_length=100)
    order_date = models.DateField()
    pickup_date = models.DateField()
    truck_options = [
        ('united', "United"),
        ('ashley', "Ashley"),
        ('serta', "Serta"),
        ('sealy', "Sealy"),
        ('freight', "Freight"),
    ]
    truck = models.CharField(
        max_length=100,
        choices=truck_options
    )
    order_types = [
        ("ph", "PH"),
        ("layaway", "Layaway")
    ]
    order_type = models.CharField(
        max_length=100,
        choices=order_types,
    )
    order_isreserved = models.BooleanField()

    def sort_by_od(self):
        return self

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Order, self).save(*args, **kwargs)

    def order_date_pretty(self):
        return self.order_date.strftime('%x')

    def pickup_date_pretty(self):
        return self.pickup_date.strftime('%x')

    def __str__(self):
        return self.customer

#class OrderForm(ModelForm):
 #   class Meta:
 #       model = Order
