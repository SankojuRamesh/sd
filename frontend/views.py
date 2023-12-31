from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, parsers, permissions, renderers, viewsets
from employeemanager.models import  EmployeeModel
from attendencemanager.models import AttendanceModel
import os
import pdfkit


# Create your views here.


def home(request):
    return render(request, 'frontend/index.html')


def login(request):
    return render(request, 'frontend/index.html')
def  dashboard(request):
    if not bool(request.user and request.user.is_authenticated) :
        ...

    return render(request, "dashboard.html") 
def  EmployeeView(request):
    uid = request.GET.get('uid')
    
    try:
        Employe_list = EmployeeModel.objects.filter(id=1)    
        return render(request, "employee.html", {'data':{} })
    except:
        return render(request, "employee.html", {'data':{} })


def  Employeedetails(request):
     
    empid = request.GET.get('id')
    if empid:
         
        Employe_list= EmployeeModel.objects.get(id=empid)
         
    return render(request, "employeedetails.html", {'data':Employe_list })





def  NewEmployeeView(request):
    Employe_list = EmployeeModel.objects.all()    
    return render(request, "newemployee.html", {'data':Employe_list })



def  AttendanceView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "attendance.html", {'data':Attendence_list })

def MyAttendanceView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "frontend/myattendance.html", {'data':Attendence_list })


def MyfamalyView(request):
    Attendence_list =    AttendanceModel.objects.all()
    return render(request, "frontend/myfamaly.html", {'data':Attendence_list })
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


def  BulkSalary(request): 
    data = {"user":request.GET.get('user')   } 
    return render(request, "bulksalary.html" , data)

 

def  EmpFamaly(request): 
    data = {"user":request.GET.get('user')   } 
    return render(request, "famaly.html" , data)




def CompanySettingsview(request):
    data = {"user":request.GET.get('user')   } 
    return render(request, "companysettings.html" , data)