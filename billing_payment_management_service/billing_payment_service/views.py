from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Bill, Payment
from .forms import BillForm, PaymentForm
from .serializers import BillSerializer, PaymentSerializer
import requests

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BillListView(View):
    def get(self, request):
        bills = Bill.objects.all()
        return render(request, 'billing_payment/bill_list.html', {'bills': bills})

class BillDetailView(View):
    def get(self, request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        return render(request, 'billing_payment/bill_detail.html', {'bill': bill})

class BillCreateView(View):
    def get(self, request):
        form = BillForm()
        return render(request, 'billing_payment/bill_form.html', {'form': form})

    def post(self, request):
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
        return render(request, 'billing_payment/bill_form.html', {'form': form})

class BillUpdateView(View):
    def get(self, request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        form = BillForm(instance=bill)
        return render(request, 'billing_payment/bill_form.html', {'form': form})

    def post(self, request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
        return render(request, 'billing_payment/bill_form.html', {'form': form})

class BillDeleteView(View):
    def get(self, request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        return render(request, 'billing_payment/bill_confirm_delete.html', {'bill': bill})

    def post(self, request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        bill.delete()
        return redirect('bill_list')

class PaymentListView(View):
    def get(self, request):
        payments = Payment.objects.all()
        return render(request, 'billing_payment/payment_list.html', {'payments': payments})

class PaymentDetailView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        return render(request, 'billing_payment/payment_detail.html', {'payment': payment})

class PaymentCreateView(View):
    def get(self, request):
        form = PaymentForm()
        bills = Bill.objects.all()
        return render(request, 'billing_payment/payment_form.html', {'form': form, 'bills': bills})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        bills = Bill.objects.all()
        return render(request, 'billing_payment/payment_form.html', {'form': form, 'bills': bills})

class PaymentUpdateView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(instance=payment)
        bills = Bill.objects.all()
        return render(request, 'billing_payment/payment_form.html', {'form': form, 'bills': bills})

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        bills = Bill.objects.all()
        return render(request, 'billing_payment/payment_form.html', {'form': form, 'bills': bills})

class PaymentDeleteView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        return render(request, 'billing_payment/payment_confirm_delete.html', {'payment': payment})

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return redirect('payment_list')

class SearchPatientView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        patients_response = requests.get(f'http://localhost:8080/patients/search/?q={query}')
        patients = patients_response.json() if patients_response.status_code == 200 else []
        return render(request, 'billing_payment/patient_search_results.html', {'patients': patients})
