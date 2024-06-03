from django.db import models

class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ('Consultation', 'Consultation'),
        ('Follow-up', 'Follow-up'),
        ('Surgery', 'Surgery'),
        # Add more as needed
    ]

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_type = models.CharField(max_length=50, choices=APPOINTMENT_TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment {self.id} - Patient {self.patient_id} with Doctor {self.doctor_id}"
