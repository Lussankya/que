from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DoctorLicense(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255)
    license_type = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_number
