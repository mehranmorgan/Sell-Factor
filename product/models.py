from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    qty=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
