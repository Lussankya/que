from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Patient, Address, Insurance
from .serializers import PatientSerializer
from .forms import PatientForm, AddressForm, InsuranceForm
from datetime import datetime
from django.http import JsonResponse
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_registration_service/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_registration_service/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        address_form = AddressForm(request.POST)
        insurance_form = InsuranceForm(request.POST)

        if patient_form.is_valid() and address_form.is_valid() and insurance_form.is_valid():
            address = address_form.save()
            insurance = insurance_form.save()
            patient = patient_form.save(commit=False)
            patient.address = address
            patient.insurance = insurance
            patient.date_of_birth = datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
            patient.save()
            return redirect('patient_list')
    else:
        patient_form = PatientForm()
        address_form = AddressForm()
        insurance_form = InsuranceForm()

    return render(request, 'patient_registration_service/patient_form.html', {
        'patient_form': patient_form,
        'address_form': address_form,
        'insurance_form': insurance_form
    })

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)
        address_form = AddressForm(request.POST, instance=patient.address)
        insurance_form = InsuranceForm(request.POST, instance=patient.insurance)

        if patient_form.is_valid() and address_form.is_valid() and insurance_form.is_valid():
            address_form.save()
            insurance_form.save()
            patient = patient_form.save(commit=False)
            patient.date_of_birth = datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
            patient.save()
            return redirect('patient_list')
    else:
        patient_form = PatientForm(instance=patient)
        address_form = AddressForm(instance=patient.address)
        insurance_form = InsuranceForm(instance=patient.insurance)

    return render(request, 'patient_registration_service/patient_form.html', {
        'patient_form': patient_form,
        'address_form': address_form,
        'insurance_form': insurance_form
    })

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        # Manually delete related records
        if patient.address:
            patient.address.delete()
        if patient.insurance:
            patient.insurance.delete()
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_registration_service/patient_confirm_delete.html', {'patient': patient})




def search_patient(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(first_name__icontains=query) | Patient.objects.filter(last_name__icontains=query)
    else:
        patients = Patient.objects.all()
    patients_list = list(patients.values('id', 'first_name', 'last_name'))
    return JsonResponse(patients_list, safe=False)
