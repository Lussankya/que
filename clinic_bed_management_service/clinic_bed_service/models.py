from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Bed(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
    ]

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    patient_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bed {self.bed_number} - {self.clinic.name}"
