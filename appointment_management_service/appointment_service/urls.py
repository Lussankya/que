from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AppointmentViewSet,
    AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView, SearchPatientView
)

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('appointments/search_patient/', SearchPatientView.as_view(), name='search_patient'),
]
