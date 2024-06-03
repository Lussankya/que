from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Staff, Department
from .forms import StaffForm, DepartmentForm
from .serializers import StaffSerializer, DepartmentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class StaffListView(View):
    def get(self, request):
        staff_members = Staff.objects.all()
        return render(request, 'staff_service/staff_list.html', {'staff_members': staff_members})

class StaffDetailView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        return render(request, 'staff_service/staff_detail.html', {'staff_member': staff_member})

class StaffCreateView(View):
    def get(self, request):
        form = StaffForm()
        departments = Department.objects.all()
        return render(request, 'staff_service/staff_form.html', {'form': form, 'departments': departments})

    def post(self, request):
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
        departments = Department.objects.all()
        return render(request, 'staff_service/staff_form.html', {'form': form, 'departments': departments})

class StaffUpdateView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        form = StaffForm(instance=staff_member)
        departments = Department.objects.all()
        return render(request, 'staff_service/staff_form.html', {'form': form, 'departments': departments})

    def post(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
        departments = Department.objects.all()
        return render(request, 'staff_service/staff_form.html', {'form': form, 'departments': departments})

class StaffDeleteView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        return render(request, 'staff_service/staff_confirm_delete.html', {'staff_member': staff_member})

    def post(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        staff_member.delete()
        return redirect('staff_list')

class DepartmentListView(View):
    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'staff_service/department_list.html', {'departments': departments})

class DepartmentDetailView(View):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        return render(request, 'staff_service/department_detail.html', {'department': department})

class DepartmentCreateView(View):
    def get(self, request):
        form = DepartmentForm()
        return render(request, 'staff_service/department_form.html', {'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        return render(request, 'staff_service/department_form.html', {'form': form})

class DepartmentUpdateView(View):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        form = DepartmentForm(instance=department)
        return render(request, 'staff_service/department_form.html', {'form': form})

    def post(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        return render(request, 'staff_service/department_form.html', {'form': form})

class DepartmentDeleteView(View):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        return render(request, 'staff_service/department_confirm_delete.html', {'department': department})

    def post(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        department.delete()
        return redirect('department_list')
