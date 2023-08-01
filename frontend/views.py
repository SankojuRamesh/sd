from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, parsers, permissions, renderers, viewsets
from employeemanager.models import  EmployeeModel
from attendencemanager.models import AttendanceModel
import os
import pdfkit


# Create your views here.



def login(request):
    return render(request, 'login.html')
def  dashboard(request):
    if not bool(request.user and request.user.is_authenticated) :
        ...

    return render(request, "dashboard.html") 
def  EmployeeView(request):
    Employe_list = EmployeeModel.objects.all()    
    return render(request, "employee.html", {'data':Employe_list })

def  NewEmployeeView(request):
    Employe_list = EmployeeModel.objects.all()    
    return render(request, "newemployee.html", {'data':Employe_list })



def  AttendanceView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "attendance.html", {'data':Attendence_list })

def  NewAttendanceView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "new_attendance.html", {'data':Attendence_list }) 
def  CompanyList(request):     
    return render(request, "companylist.html" )

 
 
def  Salary(request):     
    return render(request, "salary.html" )

def  NewSalary(request): 
    data = {"user":request.GET.get('user')   } 
    return render(request, "newsalary.html" , data)

 