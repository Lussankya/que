from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InventoryViewSet, SupplierViewSet,
    InventoryListView, InventoryDetailView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView,
    SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView
)

router = DefaultRouter()
router.register(r'inventories', InventoryViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # HTML views for Inventories
    path('inventories/', InventoryListView.as_view(), name='inventory_list'),
    path('inventories/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventories/create/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventories/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventories/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),

    # HTML views for Suppliers
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
