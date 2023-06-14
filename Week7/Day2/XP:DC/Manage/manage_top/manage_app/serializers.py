#mserializers.py
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department_detail')

    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee_detail')

    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task_detail')

    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'



