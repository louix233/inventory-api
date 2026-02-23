from rest_framework import serializers
from .models import Item, StockHistory
from .models import Category, Supplier


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ("owner", "date_added", "last_updated")


class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = "__all__"
        read_only_fields = ("updated_by", "updated_at")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
