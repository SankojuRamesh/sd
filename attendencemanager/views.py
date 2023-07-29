from django.shortcuts import render
from .  import  serializer 
from .models import AttendanceModel
from employeemanager.models import EmployeeModel
from employeemanager.serializer import EmployeeSerializer
from rest_framework import serializers

from rest_framework import generics, parsers, permissions, renderers, viewsets
from .filter import AttendanceFilter

# Create your views here.

class AttendanceViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.AttendanceSerializer
    queryset =  AttendanceModel.objects.all()
    filterset_class = AttendanceFilter
    http_method_names = ['get', 'post', 'put', 'delete']


class EmployeeAttendanceSerializer(serializers.ModelSerializer):
    
    
    def to_representation(self, instance):
        request = self.context.get('request')
        
        representation = super().to_representation(instance) 
        att = AttendanceModel.objects.filter(employee_code=instance)
        month =  request.GET.get("month", '')
        year =  request.GET.get("year", '')
        
        att= att.filter(month = month).filter(year=year)
        


        attdata =False
        if serializer.AttendanceSerializer(att, many = True).data :
            attdata =serializer.AttendanceSerializer(att, many = True).data[0] 
        print(attdata)
        representation["emp_attendance"]=  attdata
        
        return representation 
    
    class Meta:
        model = EmployeeModel
        fields ="__all__"

from django_filters import rest_framework as filters

class employeeFilterClass(filters.FilterSet):
    class Meta:
        model =EmployeeModel
        fields =['company', 'employee_code',"user"]
class EmployeeAttendance(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    queryset =      EmployeeModel.objects.all()
    serializer_class =EmployeeAttendanceSerializer
    filterset_class = employeeFilterClass

    http_method_names = ['get']



