from rest_framework import serializers
from App.models import Departments

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('__all__')


