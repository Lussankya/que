from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.patient_list, name='patient_list'),
    path('detail/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('create/', views.patient_create, name='patient_create'),
    path('update/<int:pk>/', views.patient_update, name='patient_update'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),
    path('search/', views.search_patient, name='search_patient'),
]
