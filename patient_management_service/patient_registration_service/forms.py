from django import forms
from .models import Patient, Address, Insurance

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['address', 'insurance']
        widgets = {
            'gender': forms.Select(choices=Patient.GENDER_CHOICES, attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
