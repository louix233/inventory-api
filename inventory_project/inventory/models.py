from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    threshold = models.PositiveIntegerField(default=5)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="history")
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()

    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} updated on {self.updated_at}"
