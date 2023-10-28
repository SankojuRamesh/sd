from django.shortcuts import render
from .  import  serializer 
from .models import Company, NotificatonsModel
from rest_framework import generics, parsers, permissions, renderers, viewsets
from .filters import CompanyFilter, CompanynotificationFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser



# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    # permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.CompanySerializer
    queryset =  Company.objects.all()
    filterset_class = CompanyFilter
    http_method_names = ['get', 'post', 'put', 'delete']


class notificationViewsSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    # permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.CompanyNotificationSerializer
    queryset =  NotificatonsModel.objects.all()
    filterset_class = CompanynotificationFilter
    http_method_names = ['get', 'post', 'put', 'delete']
