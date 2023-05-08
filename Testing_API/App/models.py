from django.db import models

class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)
    Faculty=models.CharField(max_length=500,blank=True)
    Hod_name=models.CharField(max_length=500,blank=True)

class Employees(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining=models.DateField()
    PhotoFileName=models.CharField(max_length=500)

