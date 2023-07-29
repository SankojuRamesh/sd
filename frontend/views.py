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

 
def  CompanyList(request):     
    return render(request, "companylist.html" )

 
 
def  Salary(request):     
    return render(request, "salary.html" )

def  NewSalary(request): 
    data = {"user":request.GET.get('user')   } 
    return render(request, "newsalary.html" , data)


def  payslip(request):

    

    # HTML and CSS code
    html_code = """ 
        <!DOCTYPE html>
        <html>
        <head>
            <title>PDF Generator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 30px;
                }
                h1 {
                    color: #007bff;
                }
                p {
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <h1>Hello, PDF World!</h1>
            <p>This is an example of generating a PDF using Python.</p>
        </body>
        </html>
        """

    # Save the HTML code to a temporary file
    with open('temp.html', 'w') as f:
        f.write(html_code)

    # Output PDF file path
    output_pdf = 'output.pdf'

    # Configure PDF options (optional)
    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
    }

    # Generate PDF from HTML file
    pdfkit.from_file('temp.html', output_pdf, options=options)

    # Remove the temporary HTML file
   
    os.remove('temp.html')

    print(f'PDF generated successfully: {output_pdf}')
        
    return render(request, "attendance.html" )