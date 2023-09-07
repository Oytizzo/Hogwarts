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
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMEBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMEBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE, primary_key=True)
