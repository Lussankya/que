from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import Doctor, Specialty, DoctorLicense
from .forms import DoctorForm, SpecialtyForm, DoctorLicenseForm
from .serializers import DoctorSerializer, DoctorLicenseSerializer, SpecialtySerializer


# API Viewsets
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorLicenseViewSet(viewsets.ModelViewSet):
    queryset = DoctorLicense.objects.all()
    serializer_class = DoctorLicenseSerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


# HTML Views
class DoctorListView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'doctor_service/doctor_list.html', {'doctors': doctors})


class DoctorDetailView(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        return render(request, 'doctor_service/doctor_detail.html', {'doctor': doctor})


class DoctorCreateView(View):
    def get(self, request):
        doctor_form = DoctorForm()
        specialty_form = SpecialtyForm()
        license_form = DoctorLicenseForm()
        return render(request, 'doctor_service/doctor_form.html', {
            'doctor_form': doctor_form,
            'specialty_form': specialty_form,
            'license_form': license_form,
        })

    def post(self, request):
        doctor_form = DoctorForm(request.POST)
        specialty_form = SpecialtyForm(request.POST)
        license_form = DoctorLicenseForm(request.POST)

        if specialty_form.is_valid() and not doctor_form.instance.specialty_id:
            specialty = specialty_form.save()
            doctor_form.instance.specialty = specialty

        if doctor_form.is_valid():
            doctor = doctor_form.save()

            if license_form.is_valid():
                license_form.instance.doctor = doctor
                license_form.save()

            return redirect('doctor_list')

        return render(request, 'doctor_service/doctor_form.html', {
            'doctor_form': doctor_form,
            'specialty_form': specialty_form,
            'license_form': license_form,
        })


class DoctorUpdateView(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor_form = DoctorForm(instance=doctor)
        specialty_form = SpecialtyForm(instance=doctor.specialty)
        license_form = DoctorLicenseForm(instance=doctor.doctorlicense_set.first())
        return render(request, 'doctor_service/doctor_form.html', {
            'doctor_form': doctor_form,
            'specialty_form': specialty_form,
            'license_form': license_form,
        })

    def post(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor_form = DoctorForm(request.POST, instance=doctor)
        specialty_form = SpecialtyForm(request.POST, instance=doctor.specialty)
        license_form = DoctorLicenseForm(request.POST, instance=doctor.doctorlicense_set.first())

        if specialty_form.is_valid():
            specialty_form.save()

        if doctor_form.is_valid():
            doctor = doctor_form.save()

            if license_form.is_valid():
                license_form.instance.doctor = doctor
                license_form.save()

            return redirect('doctor_list')

        return render(request, 'doctor_service/doctor_form.html', {
            'doctor_form': doctor_form,
            'specialty_form': specialty_form,
            'license_form': license_form,
        })


class DoctorDeleteView(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        return render(request, 'doctor_service/doctor_confirm_delete.html', {'doctor': doctor})

    def post(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return redirect('doctor_list')


class SpecialtyListView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        return render(request, 'doctor_service/specialty_list.html', {'specialties': specialties})


class SpecialtyDetailView(View):
    def get(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        return render(request, 'doctor_service/specialty_detail.html', {'specialty': specialty})


class SpecialtyCreateView(View):
    def get(self, request):
        form = SpecialtyForm()
        return render(request, 'doctor_service/specialty_form.html', {'form': form})

    def post(self, request):
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialty_list')
        return render(request, 'doctor_service/specialty_form.html', {'form': form})


class SpecialtyUpdateView(View):
    def get(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        form = SpecialtyForm(instance=specialty)
        return render(request, 'doctor_service/specialty_form.html', {'form': form})

    def post(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        form = SpecialtyForm(request.POST, instance=specialty)
        if form.is_valid():
            form.save()
            return redirect('specialty_list')
        return render(request, 'doctor_service/specialty_form.html', {'form': form})


class SpecialtyDeleteView(View):
    def get(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        return render(request, 'doctor_service/specialty_confirm_delete.html', {'specialty': specialty})

    def post(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        specialty.delete()
        return redirect('specialty_list')


class DoctorLicenseListView(View):
    def get(self, request):
        licenses = DoctorLicense.objects.all()
        return render(request, 'doctor_service/license_list.html', {'licenses': licenses})


class DoctorLicenseDetailView(View):
    def get(self, request, pk):
        license = get_object_or_404(DoctorLicense, pk=pk)
        return render(request, 'doctor_service/license_detail.html', {'license': license})


class DoctorLicenseCreateView(View):
    def get(self, request):
        form = DoctorLicenseForm()
        return render(request, 'doctor_service/license_form.html', {'form': form})

    def post(self, request):
        form = DoctorLicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('license_list')
        return render(request, 'doctor_service/license_form.html', {'form': form})


class DoctorLicenseUpdateView(View):
    def get(self, request, pk):
        license = get_object_or_404(DoctorLicense, pk=pk)
        form = DoctorLicenseForm(instance=license)
        return render(request, 'doctor_service/license_form.html', {'form': form})

    def post(self, request, pk):
        license = get_object_or_404(DoctorLicense, pk=pk)
        form = DoctorLicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            return redirect('license_list')
        return render(request, 'doctor_service/license_form.html', {'form': form})


class DoctorLicenseDeleteView(View):
    def get(self, request, pk):
        license = get_object_or_404(DoctorLicense, pk=pk)
        return render(request, 'doctor_service/license_confirm_delete.html', {'license': license})

    def post(self, request, pk):
        license = get_object_or_404(DoctorLicense, pk=pk)
        license.delete()
        return redirect('license_list')
