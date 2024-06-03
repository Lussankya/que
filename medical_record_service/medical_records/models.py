from django.db import models

class Diagnosis(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icd_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    treatment_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    drug_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient_id = models.CharField(max_length=36)  # UUID or ID as string
    record_date = models.DateField()
    doctor_id = models.CharField(max_length=36)  # UUID or ID as string
    diagnosis_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    treatment_id = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record for {self.patient_id} on {self.record_date}"

class Prescription(models.Model):
    medical_record_id = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    medication_id = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
