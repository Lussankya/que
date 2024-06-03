from django import forms
from .models import Bill, Payment

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient_id', 'total_amount', 'status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bill', 'payment_date', 'amount', 'payment_method']
