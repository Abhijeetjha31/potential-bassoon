from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App.models import Departments,Employees
from .serializers import DepartmentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def department(request):
@api_view(['GET'])
def getroutes(request):
    routes=[
        {"GET":"api/department/"},
        {"GET":"api/getbyId/id"},
    ]
    return Response(routes)



def getbyid(request,pk):
    department=Departments.objects.get(DepartmentId=pk)
    department_serializer=DepartmentSerializer(department)
    return JsonResponse(department_serializer.data,safe=False)
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Departments.objects.all().order_by("DepartmentId")
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        departmen_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=departmen_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        departmen_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=departmen_data["DepartmentId"])
        departments_serializer=DepartmentSerializer(department,data=departmen_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)




    

        