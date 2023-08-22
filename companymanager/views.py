from django.shortcuts import render
from .  import  serializer 
from .models import Company
from rest_framework import generics, parsers, permissions, renderers, viewsets
from .filters import CompanyFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser



# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.CompanySerializer
    queryset =  Company.objects.all()
    filterset_class = CompanyFilter
    http_method_names = ['get', 'post', 'put', 'delete']
