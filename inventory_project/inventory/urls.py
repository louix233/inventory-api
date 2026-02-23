from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventory.views import (
    ItemViewSet,
    StockHistoryViewSet,
    CategoryViewSet,
    SupplierViewSet
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# --------------------------------
# CREATE ROUTER BEFORE REGISTERING
# --------------------------------
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'history', StockHistoryViewSet, basename='history')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Routes
    path('api/', include(router.urls)),
]
