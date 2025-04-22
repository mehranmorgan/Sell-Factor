from django.db import models

# Create your models here.



class Seller(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    ecoCode = models.CharField(max_length=100,null=True,blank=True)
    postalCode = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


