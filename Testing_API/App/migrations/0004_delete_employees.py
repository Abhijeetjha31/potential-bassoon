# Generated by Django 4.1.7 on 2023-05-08 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_departments_faculty_alter_departments_hod_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employees',
        ),
    ]