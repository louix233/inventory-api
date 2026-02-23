from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="items")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="items")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True, related_name="items")
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="history")
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} updated"
