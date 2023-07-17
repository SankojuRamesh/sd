from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, parsers, permissions, renderers, viewsets
from employeemanager.models import  Employee
from attendencemanager.models import AttendanceModel


# Create your views here.



def login(request):
    return render(request, 'login.html')

def  dashboard(request):
    if not bool(request.user and request.user.is_authenticated) :
        ...

    return render(request, "dashboard.html")


def  EmployeeView(request):
    Employe_list = Employee.objects.all()    
    return render(request, "employee.html", {'data':Employe_list })



def  AttendanceView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "attendance.html", {'data':Attendence_list })

 
