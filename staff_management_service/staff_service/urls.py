from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StaffViewSet, DepartmentViewSet,
    StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView,
    DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
)

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # HTML views for Staff
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/create/', StaffCreateView.as_view(), name='staff_create'),
    path('staff/<int:pk>/edit/', StaffUpdateView.as_view(), name='staff_update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),

    # HTML views for Departments
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
]
