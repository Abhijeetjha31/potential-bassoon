from django.shortcuts import render
from .forms import DeparmentForm
from .models import Departments
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
import subprocess
import tempfile
from django.template.loader import render_to_string 

# Create your views here.

def open_notepad(request, id):
    data = Departments.objects.get(DepartmentId=id)
    rendered = render_to_string('details.html', {'dept': data})
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(rendered)
        temp_file.flush()
        # Open the temporary file in notepad
        subprocess.Popen(['notepad.exe', temp_file.name])
    return HttpResponse("Notepad has been opened for ID {}".format(id))

import webbrowser
import tempfile
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Departments

# def open_notepad(request, id):
#     data = Departments.objects.get(DepartmentId=id)
#     rendered = render_to_string('details.html', {'dept': data})
#     with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
#         temp_file.write(rendered)
#         temp_file.flush()
#         # Open the temporary file in Jupyter Notebook
#         notebook_url = 'http://localhost:8888/edit/untitled.txt/{}'.format(temp_file.name)
#         webbrowser.open_new_tab(notebook_url)
#     return HttpResponse("Jupyter Notebook has been opened for ID {}".format(id))

import subprocess
import nbformat
import json
from django.shortcuts import render
from django.template.loader import render_to_string

def open_notebook(request, id):
    data = Departments.objects.get(DepartmentId=id)

    # Retrieve the contents of the details.html template for the given ID
    details_page_content = render_to_string('details.html', {'data': data})

    file_name = "first"

    # for i in data:
    #     if i == id:
    #         file_name+=id

    notebook_name = file_name
            
    # Create a new .ipynb file with the given name
    nb = nbformat.v4.new_notebook()
    nb['cells'] = [nbformat.v4.new_code_cell(source=details_page_content)]
    with open(f"{notebook_name}.ipynb", 'w') as f:
        json.dump(nb, f)
    
    # Open the newly created .ipynb file in a Jupyter Notebook instance
    subprocess.Popen(['jupyter', 'notebook', f"{notebook_name}.ipynb"])

    return HttpResponse("Jupyter Notebook has been opened for ID {}".format(file_name))






def depart(request):
    dpt = Departments.objects.all().order_by("DepartmentId")
    context={
        'dpt':dpt,
    }
    return render(request,'main.html',context)



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