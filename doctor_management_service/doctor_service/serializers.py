from rest_framework import serializers
from .models import Doctor, DoctorLicense, Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorLicense
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    licenses = DoctorLicenseSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'
