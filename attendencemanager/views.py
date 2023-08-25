from django.shortcuts import render
from .  import  serializer 
from .models import AttendanceModel
from employeemanager.models import EmployeeModel
from employeemanager.serializer import EmployeeSerializer
from rest_framework import serializers
from salarymanager.models import salaryModel

from rest_framework import generics, parsers, permissions, renderers, viewsets
from rest_framework.response import Response
from .filter import AttendanceFilter
from django_filters import rest_framework as filters
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
 
import pdfkit
# Create your views here.

class AttendanceViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.AttendanceSerializer
    queryset =  AttendanceModel.objects.all()
    filterset_class = AttendanceFilter
    http_method_names = ['get', 'post', 'put', 'delete']




    def create(self, request, *args, **kwargs):
        # print(request.data.get('sal_status'))
        saldata_data = request.data.copy()
        today_date = datetime.today().strftime('%Y-%m-%d')
        
        empdata = salaryModel.objects.get(employee_code_id=saldata_data['employee_code'] )
         
        empsal = {
             "company"     :empdata.company,
            "employee_code" :empdata.employee_code.employee_code,
            "fname":empdata.employee_code.first_name,
            "lname":empdata.employee_code.last_name,
            "bank_name":empdata.employee_code.bank_name,
            "AC_no":empdata.employee_code.bank_ac_no,
            "pf_no":empdata.employee_code.pf_no,
            "sal_status"     :"",
            "updated_date"   :today_date,
            "BasicSalary"    :empdata.BasicSalary,
            "DearnessAllowance"   :empdata.DearnessAllowance,
            "HouseRentAllowance"  :empdata.HouseRentAllowance,
            "ConveyanceAllowance"  :empdata.ConveyanceAllowance,
            "MedicalAllowance"   :empdata.MedicalAllowance,
            "SpecialAllowance"   :empdata.SpecialAllowance,
            "TaxDeductedatSource"  :empdata.TaxDeductedatSource,
            "Professionaltax"  :empdata.Professionaltax,
            "pf_deductiion" :empdata.pf_deductiion,
            "esi_deduction" :empdata.esi_deduction,
            "Working_days" :saldata_data['total_days'],
            "attendance_days":saldata_data['attendance_days'],
            "month":saldata_data['month'],
            "year":saldata_data['year'],
            "GrossDeductions":float(empdata.TaxDeductedatSource)+float(empdata.Professionaltax)+float(empdata.pf_deductiion)+float(empdata.esi_deduction) ,
            "GrossEarnings":float(empdata.DearnessAllowance)+float(empdata.HouseRentAllowance)+float(empdata.HouseRentAllowance)+ 
            float(empdata.ConveyanceAllowance)+float(empdata.MedicalAllowance)+float(empdata.SpecialAllowance),
            # 'netSal' :empdata.netSal,
            
        } 
         
        html_message = render_to_string('slaray_slip.html', {'empdata': empsal})
        
         

        pdf_output_path = 'payslips/pay_slip_'+'_'+str(empdata.employee_code.employee_code)+"_"+str(saldata_data['year'])+str(saldata_data['month'])+'.pdf'

        pdf_options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }

        # Generate the PDF from the HTML string and save it to the output path
        pdfkit_config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfkit.from_string(html_message, pdf_output_path, options=pdf_options,configuration=pdfkit_config) 
        saldata_data['payslip'] = pdf_output_path
        print(saldata_data)
        serializer = self.get_serializer(data=saldata_data)
        
        serializer.is_valid(raise_exception=True)
        return super().create(serializer)

        return Response(serializer.data, status= 200 )
class EmployeeAttendanceSerializer(serializers.ModelSerializer):    
    def to_representation(self, instance):
        request = self.context.get('request')
        
        representation = super().to_representation(instance) 
        att = AttendanceModel.objects.filter(employee_code=instance)
        month =  request.GET.get("month", '')
        year =  request.GET.get("year", '')        
        att= att.filter(month = month).filter(year=year) 
        attdata =False
        
        if serializer.AttendanceSerializer(att, many = True).data :
            attdata =serializer.AttendanceSerializer(att, many = True).data[0] 
            
        representation["emp_attendance"]=  attdata        
        return representation    
    class Meta:
        model = EmployeeModel
        fields ="__all__"



class employeeFilterClass(filters.FilterSet):
    class Meta:
        model =EmployeeModel
        fields =['company', 'user']


        
class EmployeeAttendance(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated ]
    queryset =      EmployeeModel.objects.all()
    serializer_class =EmployeeAttendanceSerializer
    filterset_class = employeeFilterClass

    http_method_names = ['get']



