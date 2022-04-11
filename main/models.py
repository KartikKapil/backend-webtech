from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Total_payble_amount = models.IntegerField(default=0)
    is_vendor = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    description = models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default= 'PENDING')