from django.shortcuts import render
from .  import  serializer 
from .models import Company
from rest_framework import generics, parsers, permissions, renderers, viewsets

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.CompanySerializer
    queryset =  Company.objects.all()
    http_method_names = ['get', 'post', 'put']
