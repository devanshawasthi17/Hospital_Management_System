# Generated by Django 3.0.5 on 2020-09-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20200910_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Physician', 'Physician'), ('Anesthesiologists', 'Anesthesiologists'), ('Psychiatrist', 'Psychiatrist'), ('Neurologist', 'Neurologist'), ('Pediatrician', 'Pediatrician'), ('Ophthalmologist', 'Ophthalmologist'), ('Pathologist', 'Pathologist'), ('Gynecologist-Obstetrician', 'Gynecologist-Obstetrician'), ('Radiologist', 'Radiologist')], default='Cardiologist', max_length=50),
        ),
    ]
