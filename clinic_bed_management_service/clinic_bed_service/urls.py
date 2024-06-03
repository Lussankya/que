from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClinicViewSet, BedViewSet,
    ClinicListView, ClinicDetailView, ClinicCreateView, ClinicUpdateView, ClinicDeleteView,
    BedListView, BedDetailView, BedCreateView, BedUpdateView, BedDeleteView,
    SearchPatientView
)

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # HTML views for Clinics
    path('clinics/', ClinicListView.as_view(), name='clinic_list'),
    path('clinics/<int:pk>/', ClinicDetailView.as_view(), name='clinic_detail'),
    path('clinics/create/', ClinicCreateView.as_view(), name='clinic_create'),
    path('clinics/<int:pk>/edit/', ClinicUpdateView.as_view(), name='clinic_edit'),
    path('clinics/<int:pk>/delete/', ClinicDeleteView.as_view(), name='clinic_delete'),

    # HTML views for Beds
    path('beds/', BedListView.as_view(), name='bed_list'),
    path('beds/<int:pk>/', BedDetailView.as_view(), name='bed_detail'),
    path('beds/create/', BedCreateView.as_view(), name='bed_create'),
    path('beds/<int:pk>/edit/', BedUpdateView.as_view(), name='bed_edit'),
    path('beds/<int:pk>/delete/', BedDeleteView.as_view(), name='bed_delete'),

    # Patient search view
    path('beds/search_patient/', SearchPatientView.as_view(), name='search_patient'),
]
