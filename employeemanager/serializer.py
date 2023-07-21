from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as Employeemodel
from usermanager import models as usermodel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from usermanager.serializers import UserRoleSerializer

User = get_user_model()
class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employeemodel.Employee
        fields = '__all__'

    def create(self, validated_data):
        phone  = validated_data['phone']
        pwd = str(phone)+"_emp"        
        organization =  validated_data['company']  #Employeemodel.Employee.objects.create(**validated_data)        
        userDAta = User.objects.create_user_company(phone, pwd, organization, userType="Employee")  
        validated_data['user'] =userDAta
        return Employeemodel.Employee.objects.create(**validated_data)

 