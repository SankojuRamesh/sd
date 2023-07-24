from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as Employeemodel
from usermanager import models as usermodel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from usermanager.serializers import UserRoleSerializer
from salarymanager.serializer import salaryModelSerializer

User = get_user_model()
class EmployeeSerializer(serializers.ModelSerializer):      
    
    class Meta:
        model = Employeemodel.EmployeeModel
        fields ="__all__"
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)        
        print(salaryModelSerializer(instance.empsalary, many=True).data)   
        salary_data  =  salaryModelSerializer(instance.empsalary, many=True).data
        
        if salary_data:
            data =  salary_data
        else:            
            data = "nosalary"         
        representation.update({"empsalary":  data})        
        return representation
    
 


    def create(self, validated_data):
        print(validated_data)
        phone  = validated_data['phone']
        pwd = str(phone)+"_emp"        
        organization =  validated_data['company']  #Employeemodel.Employee.objects.create(**validated_data)        
        userDAta = User.objects.create_user_company(phone, pwd, organization, userType="Employee")  
        validated_data['user'] =userDAta
        return Employeemodel.EmployeeModel.objects.create(**validated_data)

 