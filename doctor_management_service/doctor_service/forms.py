from django import forms
from .models import Doctor, Specialty, DoctorLicense

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'phone', 'email', 'department']

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = ['name', 'description']

class DoctorLicenseForm(forms.ModelForm):
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DoctorLicense
        fields = ['license_number', 'license_type', 'issued_by', 'issue_date', 'expiry_date']
