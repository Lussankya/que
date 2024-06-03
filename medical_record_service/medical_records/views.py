import requests
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import MedicalRecord, Diagnosis, Treatment, Prescription, Medication
from .serializers import MedicalRecordSerializer, DiagnosisSerializer, TreatmentSerializer, PrescriptionSerializer, \
    MedicationSerializer
from .forms import MedicalRecordForm, DiagnosisForm, TreatmentForm, PrescriptionForm, MedicationForm


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


def medical_record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'medical_records/medical_record_list.html', {'records': records})


def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'medical_records/medical_record_detail.html', {'record': record})


def medical_record_create(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        try:
            doctors_response = requests.get('http://localhost:8082/api/doctors/')
            doctors_response.raise_for_status()
            doctors = doctors_response.json()
        except (requests.RequestException, ValueError):
            doctors = []
        form = MedicalRecordForm()
    return render(request, 'medical_records/medical_record_form.html', {
        'form': form,
        'doctors': doctors,
        'diagnosis_form': DiagnosisForm(),
        'treatment_form': TreatmentForm(),
    })

def medical_record_update(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        try:
            doctors_response = requests.get('http://localhost:8082/api/doctors/')
            doctors_response.raise_for_status()
            doctors = doctors_response.json()
        except (requests.RequestException, ValueError):
            doctors = []
        form = MedicalRecordForm(instance=record)
    return render(request, 'medical_records/medical_record_form.html', {
        'form': form,
        'doctors': doctors,
        'diagnosis_form': DiagnosisForm(),
        'treatment_form': TreatmentForm(),
    })


def medical_record_delete(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('medical_record_list')
    return render(request, 'medical_records/medical_record_confirm_delete.html', {'record': record})


def search_patient(request):
    query = request.GET.get('q')
    if query:
        try:
            response = requests.get(f'http://localhost:8080/patients/search/?q={query}')
            response.raise_for_status()
            patients = response.json()
        except requests.RequestException as e:
            print(e)
            patients = []
    else:
        patients = []
    return render(request, 'medical_records/search_patient.html', {'patients': patients})


def create_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_create')
    else:
        form = DiagnosisForm()
    return render(request, 'medical_records/diagnosis_form.html', {'form': form})


def create_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_create')
    else:
        form = TreatmentForm()
    return render(request, 'medical_records/treatment_form.html', {'form': form})


def create_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_prescription')
    else:
        form = MedicationForm()
    return render(request, 'medical_records/medication_form.html', {'form': form})


def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'medical_records/prescription_form.html', {
        'form': form,
        'medication_form': MedicationForm(),
    })


def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'medical_records/prescription_detail.html', {'prescription': prescription})


def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'medical_records/prescription_list.html', {'prescriptions': prescriptions})
