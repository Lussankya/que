from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Clinic, Bed
from .forms import ClinicForm, BedForm
from .serializers import ClinicSerializer, BedSerializer
import requests

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class ClinicListView(View):
    def get(self, request):
        clinics = Clinic.objects.all()
        return render(request, 'clinic_bed/clinic_list.html', {'clinics': clinics})

class ClinicDetailView(View):
    def get(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        return render(request, 'clinic_bed/clinic_detail.html', {'clinic': clinic})

class ClinicCreateView(View):
    def get(self, request):
        form = ClinicForm()
        return render(request, 'clinic_bed/clinic_form.html', {'form': form})

    def post(self, request):
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinic_list')
        return render(request, 'clinic_bed/clinic_form.html', {'form': form})

class ClinicUpdateView(View):
    def get(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        form = ClinicForm(instance=clinic)
        return render(request, 'clinic_bed/clinic_form.html', {'form': form})

    def post(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('clinic_list')
        return render(request, 'clinic_bed/clinic_form.html', {'form': form})

class ClinicDeleteView(View):
    def get(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        return render(request, 'clinic_bed/clinic_confirm_delete.html', {'clinic': clinic})

    def post(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        clinic.delete()
        return redirect('clinic_list')

class BedListView(View):
    def get(self, request):
        beds = Bed.objects.all()
        return render(request, 'clinic_bed/bed_list.html', {'beds': beds})

class BedDetailView(View):
    def get(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        return render(request, 'clinic_bed/bed_detail.html', {'bed': bed})

class BedCreateView(View):
    def get(self, request):
        form = BedForm()
        clinics = Clinic.objects.all()
        return render(request, 'clinic_bed/bed_form.html', {'form': form, 'clinics': clinics})

    def post(self, request):
        form = BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bed_list')
        clinics = Clinic.objects.all()
        return render(request, 'clinic_bed/bed_form.html', {'form': form, 'clinics': clinics})

class BedUpdateView(View):
    def get(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        form = BedForm(instance=bed)
        clinics = Clinic.objects.all()
        return render(request, 'clinic_bed/bed_form.html', {'form': form, 'clinics': clinics})

    def post(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        form = BedForm(request.POST, instance=bed)
        if form.is_valid():
            form.save()
            return redirect('bed_list')
        clinics = Clinic.objects.all()
        return render(request, 'clinic_bed/bed_form.html', {'form': form, 'clinics': clinics})

class BedDeleteView(View):
    def get(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        return render(request, 'clinic_bed/bed_confirm_delete.html', {'bed': bed})

    def post(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        bed.delete()
        return redirect('bed_list')

class SearchPatientView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        patients_response = requests.get(f'http://localhost:8080/patients/search/?q={query}')
        patients = patients_response.json() if patients_response.status_code == 200 else []
        return render(request, 'clinic_bed/patient_search_results.html', {'patients': patients})
