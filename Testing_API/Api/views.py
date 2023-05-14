# views.py
from rest_framework import viewsets
from App.models import Departments
from Api.serializers import DepartmentSerializer
from django.http import HttpResponse
import subprocess

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all().order_by("DepartmentId")
    serializer_class = DepartmentSerializer









    

        