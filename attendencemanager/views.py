from django.shortcuts import render
from .  import  serializer 
from .models import AttendanceModel
from rest_framework import generics, parsers, permissions, renderers, viewsets
# from .filters import CompanyFilter

# Create your views here.

class AttendanceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.AttendanceSerializer
    queryset =  AttendanceModel.objects.all()
    #filterset_class = CompanyFilter
    http_method_names = ['get', 'post', 'put', 'delete']
