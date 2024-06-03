from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Inventory, Supplier
from .forms import InventoryForm, SupplierForm
from .serializers import InventorySerializer, SupplierSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class InventoryListView(View):
    def get(self, request):
        inventories = Inventory.objects.all()
        return render(request, 'inventory_supplier_service/inventory_list.html', {'inventories': inventories})

class InventoryDetailView(View):
    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        return render(request, 'inventory_supplier_service/inventory_detail.html', {'inventory': inventory})

class InventoryCreateView(View):
    def get(self, request):
        form = InventoryForm()
        return render(request, 'inventory_supplier_service/inventory_form.html', {'form': form})

    def post(self, request):
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
        return render(request, 'inventory_supplier_service/inventory_form.html', {'form': form})

class InventoryUpdateView(View):
    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        form = InventoryForm(instance=inventory)
        return render(request, 'inventory_supplier_service/inventory_form.html', {'form': form})

    def post(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
        return render(request, 'inventory_supplier_service/inventory_form.html', {'form': form})

class InventoryDeleteView(View):
    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        return render(request, 'inventory_supplier_service/inventory_confirm_delete.html', {'inventory': inventory})

    def post(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        inventory.delete()
        return redirect('inventory_list')

class SupplierListView(View):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'inventory_supplier_service/supplier_list.html', {'suppliers': suppliers})

class SupplierDetailView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, 'inventory_supplier_service/supplier_detail.html', {'supplier': supplier})

class SupplierCreateView(View):
    def get(self, request):
        form = SupplierForm()
        return render(request, 'inventory_supplier_service/supplier_form.html', {'form': form})

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        return render(request, 'inventory_supplier_service/supplier_form.html', {'form': form})

class SupplierUpdateView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        form = SupplierForm(instance=supplier)
        return render(request, 'inventory_supplier_service/supplier_form.html', {'form': form})

    def post(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        return render(request, 'inventory_supplier_service/supplier_form.html', {'form': form})

class SupplierDeleteView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, 'inventory_supplier_service/supplier_confirm_delete.html', {'supplier': supplier})

    def post(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.delete()
        return redirect('supplier_list')
