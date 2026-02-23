from django.contrib import admin
from .models import Item, StockHistory

admin.site.register(Item)
admin.site.register(StockHistory)
