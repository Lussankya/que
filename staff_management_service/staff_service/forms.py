from django import forms
from .models import Staff, Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'role', 'department', 'phone', 'email', 'employment_date']
