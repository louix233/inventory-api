from rest_framework import serializers
from .models import Item, StockHistory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]


class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = "__all__"
        read_only_fields = ["updated_by", "updated_at"]
