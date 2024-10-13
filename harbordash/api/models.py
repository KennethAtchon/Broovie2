from django.db import models
from django.utils import timezone

# Admin User Model
# Put most of your logic in models
class AdminUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

# Project Model
class Project(models.Model):
    admin_user = models.OneToOneField(AdminUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Regular User Model
class RegularUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

# Item Model
class Item(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    precise_description = models.JSONField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    images = models.JSONField(blank=True, null=True)
    options_images = models.JSONField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    product_types = models.CharField(max_length=255, blank=True, null=True)
    special = models.CharField(max_length=255, blank=True, null=True)
    quantity_in_stock = models.IntegerField()
    shipping_details = models.JSONField(blank=True, null=True)
    options_product = models.JSONField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    on_sale = models.BooleanField(default=False)
    related_products = models.JSONField(blank=True, null=True)
    measurements = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Order Model
class Order(models.Model):
    user = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    stripe_session_id = models.CharField(max_length=255)
    products = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=255)
    shipping_address = models.JSONField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=255, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

# Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OrderItem {self.id} - {self.item.name}"
