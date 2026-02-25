from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import F
from .models import Item, StockHistory
from .serializers import ItemSerializer, StockHistorySerializer


class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(created_by=self.request.user)


class LowStockView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(
            created_by=self.request.user,
            quantity__lt=F("threshold")
        )


class CategoryFilterView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cat = self.kwargs.get("category")
        return Item.objects.filter(
            created_by=self.request.user, category__iexact=cat
        )


class StockHistoryListView(generics.ListAPIView):
    serializer_class = StockHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StockHistory.objects.filter(item_id=self.kwargs["item_id"])


class StockHistoryCreateView(generics.CreateAPIView):
    serializer_class = StockHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user)
