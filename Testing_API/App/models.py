from django.db import models
import json

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    Faculty = models.CharField(max_length=500)
    Hod_name = models.CharField(max_length=500)
