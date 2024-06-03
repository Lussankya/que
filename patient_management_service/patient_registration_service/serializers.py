from rest_framework import serializers
from .models import Patient, Address, Insurance

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    insurance = InsuranceSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        insurance_data = validated_data.pop('insurance')
        address = Address.objects.create(**address_data)
        insurance = Insurance.objects.create(**insurance_data)
        patient = Patient.objects.create(address=address, insurance=insurance, **validated_data)
        return patient

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        insurance_data = validated_data.pop('insurance')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.emergency_contact_name = validated_data.get('emergency_contact_name', instance.emergency_contact_name)
        instance.emergency_contact_phone = validated_data.get('emergency_contact_phone', instance.emergency_contact_phone)
        instance.save()

        address = instance.address
        address.street = address_data.get('street', address.street)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.zip_code = address_data.get('zip_code', address.zip_code)
        address.country = address_data.get('country', address.country)
        address.save()

        insurance = instance.insurance
        insurance.provider = insurance_data.get('provider', insurance.provider)
        insurance.policy_number = insurance_data.get('policy_number', insurance.policy_number)
        insurance.coverage_details = insurance_data.get('coverage_details', insurance.coverage_details)
        insurance.save()

        return instance
