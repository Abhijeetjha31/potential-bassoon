# Generated by Django 4.1.7 on 2023-05-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_departments_faculty_departments_hod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='Faculty',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='departments',
            name='Hod_name',
            field=models.CharField(max_length=500),
        ),
    ]
