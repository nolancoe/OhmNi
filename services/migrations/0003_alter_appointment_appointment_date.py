# Generated by Django 4.0.4 on 2022-04-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_appointment_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(verbose_name='Appointment Date'),
        ),
    ]