from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    ROLE_CHOICES = [
        ('Nurse', 'Nurse'),
        ('Technician', 'Technician'),
        ('Admin', 'Admin'),
        ('Dokutah', 'Dokutah'),
        # Add more roles as needed
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    employment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
