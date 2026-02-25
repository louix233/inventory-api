from django.urls import path
from .views import (
    ItemListCreateView,
    ItemDetailView,
    LowStockView,
    CategoryFilterView,
    StockHistoryListView,
    StockHistoryCreateView
)

urlpatterns = [
    path("items/", ItemListCreateView.as_view()),
    path("items/<int:pk>/", ItemDetailView.as_view()),
    path("items/low-stock/", LowStockView.as_view()),
    path("items/category/<str:category>/", CategoryFilterView.as_view()),

    path("items/<int:item_id>/history/", StockHistoryListView.as_view()),
    path("items/<int:item_id>/history/add/", StockHistoryCreateView.as_view()),
]
