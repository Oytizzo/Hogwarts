from django.db import models


class Promotion(models.Model):
    # product_set <default>
    # products <if related_name="products">
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(to="Product", on_delete=models.SET_NULL, null=True, related_name="+")


class Product(models.Model):
    # sku = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)    #varchar(255)
    slug = models.SlugField()
    description = models.TextField()            #text
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)     # 999999.99
    inventory = models.IntegerField()
    first_entry = models.DateTimeField(auto_now_add=True, null=True)   # auto_now_add updates one time when first product was added
    last_update = models.DateTimeField(auto_now=True)   # auto_now update everytime product updates
    Collection = models.ForeignKey(to=Collection, on_delete=models.PROTECT)
    # promotions = models.ManyToManyField(to=Promotion, related_name="products")
    promotions = models.ManyToManyField(to=Promotion)


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
    birth_date = models.DateField(null=True)
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
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    qantity = models.PositiveSmallIntegerField()
