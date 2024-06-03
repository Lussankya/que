from django import forms
from .models import MedicalRecord, Diagnosis, Treatment, Prescription, Medication

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'patient_id': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'doctor_id': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis_id': forms.Select(attrs={'class': 'form-control'}),
            'treatment_id': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'medical_record_id': forms.Select(attrs={'class': 'form-control'}),
            'medication_id': forms.Select(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
