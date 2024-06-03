from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.medical_record_list, name='medical_record_list'),
    path('detail/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('create/', views.medical_record_create, name='medical_record_create'),
    path('update/<int:pk>/', views.medical_record_update, name='medical_record_update'),
    path('delete/<int:pk>/', views.medical_record_delete, name='medical_record_delete'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('create_diagnosis/', views.create_diagnosis, name='create_diagnosis'),
    path('create_treatment/', views.create_treatment, name='create_treatment'),
    path('create_medication/', views.create_medication, name='create_medication'),
    path('create_prescription/', views.create_prescription, name='create_prescription'),
    path('prescription_detail/<int:pk>/', views.prescription_detail, name='prescription_detail'),
    path('prescription_list/', views.prescription_list, name='prescription_list'),
]
