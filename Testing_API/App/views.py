from django.shortcuts import render
from .forms import DeparmentForm
from .models import Departments
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
# Create your views here.


def depart(request):
    dpt = Departments.objects.all().order_by("DepartmentId")
    context={
        'dpt':dpt,
    }
    return render(request,'main.html',context)

def create(request):
    form=DeparmentForm()
    return render(request,{"form":form})

def add(request):
    form=DeparmentForm()
    if request.method=="POST":
        form = DeparmentForm(request.POST)
        if form.is_valid():
            # Save the updated department to the database
            form.save()

            # Redirect to a success page
            return redirect('depart-data')
    return render(request,"addEdit.html",{"form":form})



def delete(request, id):
    # Retrieve the object to be deleted, or return a 404 if it doesn't exist
    my_object = get_object_or_404(Departments, DepartmentId=id)

    # Delete the object
    my_object.delete()

    # Redirect to a success page
    return redirect('depart-data')

def edit(request, pk):
   
    # Retrieve the department object to be edited, or return a 404 if it doesn't exist
    department = get_object_or_404(Departments, pk=pk)

    if request.method == "POST":
        # Populate the form with the POST data and the existing department instance
        form = DeparmentForm(request.POST, instance=department)

        if form.is_valid():
            # Save the updated department to the database
            department = form.save()

            # Redirect to a success page
            messages.success(request,"Edited Successfully")
            return redirect('depart-data')
    # Create a new form instance pre-populated with the existing department data
    form = DeparmentForm(instance=department)

    return render(request, "addEdit.html", {"form": form,"id":pk})

def detail(request, pk):
    # Retrieve the instance with the specified pk
    dept = get_object_or_404(Departments, DepartmentId=pk)
    
    context = {
        'dept': dept,
    }
    return render(request, 'details.html', context)