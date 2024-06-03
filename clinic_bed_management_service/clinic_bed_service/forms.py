from django import forms
from .models import Clinic, Bed

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'location', 'phone']

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ['clinic', 'bed_number', 'status', 'patient_id']
