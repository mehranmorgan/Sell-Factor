from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
