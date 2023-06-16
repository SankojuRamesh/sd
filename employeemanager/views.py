from django.shortcuts import render
from .  import  serializer 
from .models import Employee
from rest_framework import generics, parsers, permissions, renderers, viewsets
# from .filters import CompanyFilter

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.EmployeeSerializer
    queryset =  Employee.objects.all()
    #filterset_class = CompanyFilter
    http_method_names = ['get', 'post', 'put', 'delete']
