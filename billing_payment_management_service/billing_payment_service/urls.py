from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BillViewSet, PaymentViewSet,
    BillListView, BillDetailView, BillCreateView, BillUpdateView, BillDeleteView,
    PaymentListView, PaymentDetailView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView,
    SearchPatientView
)

router = DefaultRouter()
router.register(r'bills', BillViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # HTML views for Bills
    path('bills/', BillListView.as_view(), name='bill_list'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bill_detail'),
    path('bills/create/', BillCreateView.as_view(), name='bill_create'),
    path('bills/<int:pk>/edit/', BillUpdateView.as_view(), name='bill_edit'),
    path('bills/<int:pk>/delete/', BillDeleteView.as_view(), name='bill_delete'),

    # HTML views for Payments
    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment_edit'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),

    # Patient search view
    path('payments/search_patient/', SearchPatientView.as_view(), name='search_patient'),
]
