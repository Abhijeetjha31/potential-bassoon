from .models import Departments

from django import forms
from django.forms import ModelForm

class DeparmentForm(ModelForm):
    class Meta:
        model=Departments
        fields="__all__"
