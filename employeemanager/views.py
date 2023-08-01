from django.shortcuts import render,HttpResponse
from .  import  serializer 
from .models import EmployeeModel
from rest_framework import generics, parsers, permissions, renderers, viewsets
from .filters import employeeFilter
from rest_framework.views import  APIView
import pandas as pd
from django.http import HttpResponse, FileResponse
from rest_framework.parsers import FileUploadParser,FileUploadParser
from django.conf import settings
import os
from rest_framework import status
from rest_framework.response import Response
 


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user        
        queryset = EmployeeModel.objects.filter(company=user.company)
        return queryset
    
    permission_classes = [permissions.IsAuthenticated ]
    serializer_class = serializer.EmployeeSerializer
    queryset =  EmployeeModel.objects.all()
    
    filterset_class = employeeFilter
    http_method_names = ['get', 'post', 'put', 'delete']


class  DownloadViewSet(APIView):
    def get(self, request):
        company = request.GET.get('company')
        file_path = os.path.join(settings.MEDIA_ROOT, "test.xlsx")
         

         
        # Create a response object with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="test.xlsx"'

        # Write the DataFrame to the response object as an Excel file
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename=test.xlsx'
                return response
        else:
            return HttpResponse("File not found", status=404)
         
        return response



class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    serializer_class =  serializer.FileUploadSerializer
    def post(self, request, *args, **kwargs):
        fileserializer = serializer.FileUploadSerializer(data=request.data)
         

        if fileserializer.is_valid():
            uploaded_file = fileserializer.validated_data['file']

            # Save the file to the desired location (you can also process the file here)
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(file_path, 'wb') as file:
                for chunk in uploaded_file.chunks():
                    file.write(chunk)

            return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(fileserializer.errors, status=status.HTTP_400_BAD_REQUEST)