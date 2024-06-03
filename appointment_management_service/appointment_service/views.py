from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer
import requests

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentListView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'appointment_service/appointment_list.html', {'appointments': appointments})

class AppointmentDetailView(View):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        return render(request, 'appointment_service/appointment_detail.html', {'appointment': appointment})

class AppointmentCreateView(View):
    def get(self, request):
        form = AppointmentForm()
        doctors_response = requests.get('http://localhost:8082/api/doctors/')
        doctors = doctors_response.json() if doctors_response.status_code == 200 else []
        return render(request, 'appointment_service/appointment_form.html', {'form': form, 'doctors': doctors})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
        doctors_response = requests.get('http://localhost:8082/api/doctors/')
        doctors = doctors_response.json() if doctors_response.status_code == 200 else []
        return render(request, 'appointment_service/appointment_form.html', {'form': form, 'doctors': doctors})

class AppointmentUpdateView(View):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentForm(instance=appointment)
        doctors_response = requests.get('http://localhost:8082/api/doctors/')
        doctors = doctors_response.json() if doctors_response.status_code == 200 else []
        return render(request, 'appointment_service/appointment_form.html', {'form': form, 'doctors': doctors})

    def post(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
        doctors_response = requests.get('http://localhost:8082/api/doctors/')
        doctors = doctors_response.json() if doctors_response.status_code == 200 else []
        return render(request, 'appointment_service/appointment_form.html', {'form': form, 'doctors': doctors})

class AppointmentDeleteView(View):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        return render(request, 'appointment_service/appointment_confirm_delete.html', {'appointment': appointment})

    def post(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return redirect('appointment_list')

class SearchPatientView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        patients_response = requests.get(f'http://localhost:8080/patients/search/?q={query}')
        patients = patients_response.json() if patients_response.status_code == 200 else []
        return render(request, 'appointment_service/patient_search_results.html', {'patients': patients})
