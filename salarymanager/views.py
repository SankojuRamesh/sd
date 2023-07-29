from django.shortcuts import render
from .  import  serializer 
from .models import salaryModel
from rest_framework import generics, parsers, permissions, renderers, viewsets
 
from rest_framework.response import Response
from openpyxl import Workbook

# from .filters import CompanyFilter

# Create your views here.

class salaryViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.salaryModelSerializer
    queryset =  salaryModel.objects.all()
    #filterset_class = CompanyFilter
    http_method_names = ['get', 'post', 'put', 'delete']




class YourModelViewSet(viewsets.ModelViewSet):
    queryset = salaryModel.objects.all()
    serializer_class = serializer.salaryModelSerializer

    def download_excel(self, request):
        data = salaryModel.objects.all()
        serializerdata = serializer.salaryModelSerializer(data, many=True)

        # Create an Excel workbook and worksheet
        wb = Workbook()
        ws = wb.active

        # Write header row
        header = ["employee_code", "company", "BasicSalary"]  # Replace with your model fields
        ws.append(header)

        # Write data rows
        for item in serializerdata.data:
            row = [item["employee_code"], item["company"], item["BasicSalary"]]  # Replace with your model fields
            ws.append(row)

        # Save the workbook to a response
        response = Response(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=your_data.xlsx'
        wb.save('your_data.xlsx')
        print(response)

        return response
