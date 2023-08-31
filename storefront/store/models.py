from django.db import models

# Create your models here.
class Product(models.Model):
    # sku = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)    #varchar(255)
    description = models.TextField()            #text
    price = models.DecimalField(max_digits=6, decimal_places=2)     # 999999.99
    inventory = models.IntegerField()
    first_entry = models.DateTimeField(auto_now_add=True)   # auto_now_add updates one time when first product was added
    last_update = models.DateTimeField(auto_now=True)   # auto_now update everytime product updates


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField(null=True)
