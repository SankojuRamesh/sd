from django.shortcuts import render,HttpResponse
from .  import  serializer 
from .models import EmployeeModel, EmpFamaly
from companymanager.models import Company
from rest_framework import generics, parsers, permissions, renderers, viewsets

from .filters import employeeFilter, employeeFamalyFilter
from rest_framework.views import  APIView
import pandas as pd
from django.http import HttpResponse, FileResponse
from rest_framework.parsers import FileUploadParser,FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.conf import settings
import os
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from django.template.loader import render_to_string
import pdfkit  
 
User = get_user_model()

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.EmployeeSerializer
    queryset =  EmployeeModel.objects.all() 
    filterset_class = employeeFilter
    http_method_names = ['get', 'post', 'put', 'delete']


class EmployeeFamalyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class = serializer.EmployeeFmalaySerializer
    queryset =  EmpFamaly.objects.all() 
    filterset_class = employeeFamalyFilter
    http_method_names = ['get', 'post', 'put', 'delete']


class  DownloadViewSet(APIView):
    def get(self, request):
        company = request.GET.get('company')
        file_path = os.path.join(settings.MEDIA_ROOT, "employee_list.csv")  
        # Create a response object with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="employee_list.csv"' 
        # Write the DataFrame to the response object as an Excel file
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename=employee_list.csv'
                return response
        else:
            return HttpResponse("File not found", status=404)
         
        return response


class FileUploadView(APIView):
   parser_classes = (MultiPartParser,FormParser,JSONParser)
   def post(self, request, format=None):
        serializer_data = serializer.FileUploadSerializer(data=request.data)
        
        if serializer_data.is_valid():
             
            uploaded_file = serializer_data.validated_data['file'] 
            df = pd.read_csv(uploaded_file,  skipinitialspace=True).fillna('--')
            df.columns = df.columns.str.replace(' ', '')
            df.columns = df.columns.str.rsplit('/', n=1).str[-1]
            print( df.columns )
             


            dict = {}
            for index, row in df.iterrows():
                

                ac = row['BankAccountNo,IFSCCode']
                ifsc =  row['BankAccountNo,IFSCCode']
                if row['BankAccountNo,IFSCCode'] != 'NOT AVAIALABLE':
                    ac = row['BankAccountNo,IFSCCode'].split(",")[0]
                    ifsc= row['BankAccountNo,IFSCCode'].split(",")[1]


                companyobj = Company.objects.get(id=request.data['company'])
                 
                if not  row['AADHAAR']  == 'NOT AVAILABLE':
                    data = {"company" :  companyobj,
                        "first_name" :  row['Name'] , 
                        "last_name"   :  row['Name'].split(" ")[1] ,  
                        "phone"     :  row['Mobile'] ,  
                        "husband_Father"   :  row["Husband'sName"] ,   
                        "designation"   :  row['Name'],   
                        "relation_name"   :  row['Relation'],   
                        "employee_code"  :  row['MemberID']  , 
                        "gender"  :  row['Gender']   ,
                        "blood_group"   :  row['Name'] ,  
                        "contact_number"   :  row['Mobile']   ,
                        "dob"     :  row['DoB']   ,
                        "date_of_joining"   :  row['DoJ']   ,
                        "email"    :  row['EmailID']  , 
                        "aadhar_number"    :  row['AADHAAR']   ,
                        "uan_number"    :  row['UAN']  , 
                        "pan_number"     :  row['PAN'] ,  
                        "pf_account"    :   row['UAN']  ,
                        "pf_no"     : row['UAN'],
                        "pf_date"     :  '--',
                        "basic_salary"     :  '--',
                        "bank_ac_no"     :ac ,
                        "bank_name"     :  '--',
                        "ifsc_code"     : ifsc  ,
                        "Image"         : "/freelogo.png",
                    }
                    # 8341000230
                    
                    phone  = str(row['Mobile'])+str(row['AADHAAR'][-4:]) 
                    pwd = str( row['Mobile'])+str(row['AADHAAR'][-4:])+"_emp"        
                        
                    userDAta = User.objects.create_user_company(phone, pwd, companyobj, userType="Employee")  
                    data['user_id'] = userDAta.id
                    EmployeeModel(**data).save()
               
                 
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED) 
   


class EmployeeIdcardsviewSet(APIView):

    def get(self, request): 
        companyid = request.GET.get('company')
        employee = EmployeeModel.objects.filter(company =companyid )
        print(employee)
        if not employee:
            return HttpResponse("Employes not found", status=404)
        
        html_string = render_to_string('table.html', {"data":employee})

        pdfkit.from_string(html_string, 'out.pdf')
        company = request.GET.get('company') 
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="out.pdf"'
        file_path = os.path.join(settings.MEDIA_ROOT, "out.pdf")  
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename=out.pdf'
                return response
        else:
            return HttpResponse("File not found", status=404)


