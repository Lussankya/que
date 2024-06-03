from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewSet, DoctorLicenseViewSet, SpecialtyViewSet,
    DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    SpecialtyListView, SpecialtyDetailView, SpecialtyCreateView, SpecialtyUpdateView, SpecialtyDeleteView,
    DoctorLicenseListView, DoctorLicenseDetailView, DoctorLicenseCreateView, DoctorLicenseUpdateView, DoctorLicenseDeleteView
)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'doctor_licenses', DoctorLicenseViewSet)
router.register(r'specialties', SpecialtyViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # HTML views for Doctors
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    # HTML views for Specialties
    path('specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('specialties/<int:pk>/', SpecialtyDetailView.as_view(), name='specialty_detail'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty_create'),
    path('specialties/<int:pk>/edit/', SpecialtyUpdateView.as_view(), name='specialty_update'),
    path('specialties/<int:pk>/delete/', SpecialtyDeleteView.as_view(), name='specialty_delete'),

    # HTML views for Licenses
    path('licenses/', DoctorLicenseListView.as_view(), name='license_list'),
    path('licenses/<int:pk>/', DoctorLicenseDetailView.as_view(), name='license_detail'),
    path('licenses/create/', DoctorLicenseCreateView.as_view(), name='license_create'),
    path('licenses/<int:pk>/edit/', DoctorLicenseUpdateView.as_view(), name='license_update'),
    path('licenses/<int:pk>/delete/', DoctorLicenseDeleteView.as_view(), name='license_delete'),
]
