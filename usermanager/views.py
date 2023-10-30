# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth import get_user_model
from rest_framework import generics, parsers, permissions, status,renderers, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views
from django.shortcuts import HttpResponse,render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from companymanager.models import Company
 

 
from . import models, serializers

User = get_user_model()
 

class SignInView(jwt_views.TokenObtainPairView):
    """
    SignIn Endpoint using email & password
    Response: access & refresh tokens
    """

    serializer_class = serializers.SignInSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserRoleListView(generics.ListAPIView):
    """
    Only Admins can access this API
    """

    queryset = models.UserRole.objects.filter(name__in=['SuperAdmin','Admin', "SubAdmin",  'Employee'])
    serializer_class = serializers.UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated ]

def Logout(request):
    print(dir(request.user))
    # RefreshToken(token).blacklist()
    return HttpResponse({})

@csrf_exempt
def adminslist(request):
    phoneno = request.GET.get("phoneno") 
    companyid = request.GET.get("company")
    name = request.GET.get("name")
    if phoneno:        
        companyobj = Company.objects.get(id=companyid)
        userDAta = User.objects.create_subadmin_company(phoneno, "admin@123", companyobj, userType="SubAdmin", name=name) 
     
    companyid = request.GET.get("cid")
    adminlist =  User.objects.filter(company_id=companyid).filter(roles_id = 3)
    
    return render(request, "adminlist.html", {'adminlist':adminlist })
    
 