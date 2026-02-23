from django.db import models
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.mail import send_mail

from .models import Item, StockHistory, Category, Supplier
from .serializers import (
    ItemSerializer,
    StockHistorySerializer,
    CategorySerializer,
    SupplierSerializer
)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']
    search_fields = ['name', 'description']

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_items = self.get_queryset().filter(quantity__lt=models.F('threshold'))
        serializer = self.get_serializer(low_items, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        old_item = self.get_object()
        old_quantity = old_item.quantity

        updated_item = serializer.save()

        # Log stock history
        if old_quantity != updated_item.quantity:
            StockHistory.objects.create(
                item=updated_item,
                old_quantity=old_quantity,
                new_quantity=updated_item.quantity,
                updated_by=self.request.user
            )

        # Low stock email alert
        if updated_item.quantity < updated_item.threshold:
            send_mail(
                subject="Low Stock Alert",
                message=f"{updated_item.name} is low on stock.",
                from_email="noreply@inventory.com",
                recipient_list=[self.request.user.email],
            )

    @action(detail=False, methods=['get'])
    def report(self, request):
        queryset = self.get_queryset()

        total_items = queryset.count()
        total_quantity = sum(item.quantity for item in queryset)
        total_value = sum(item.quantity * item.price for item in queryset)

        return Response({
            "total_items": total_items,
            "total_quantity": total_quantity,
            "total_inventory_value": total_value
        })


class StockHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StockHistory.objects.filter(updated_by=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
