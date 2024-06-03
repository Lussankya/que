from django import forms
from .models import Inventory, Supplier

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'quantity', 'unit', 'supplier', 'expiry_date']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'phone', 'email', 'address']
