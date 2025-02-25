# Generated by Django 5.0.6 on 2024-06-01 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_registration_service', '0002_alter_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient_registration_service.address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient_registration_service.insurance'),
            preserve_default=False,
        ),
    ]
