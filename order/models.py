from django.db import models
from django.db.models import Sum

from customer.models import Customer
from product.models import Product
from seller.models import Seller


class Order(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='orders')
    date = models.DateField(auto_now_add=True)
    @property
    def total(self):
        return self.items.aggregate(total=Sum('row_price'))['total']

    def __str__(self):
        return f'{self.customer.name}, {self.date}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    row_price = models.IntegerField(null=True, blank=True)
    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.row_price=int(self.qty)*int(self.product.price)
        super().save()


    def __str__(self):
        return f'{self.product.name}, {self.qty}'
