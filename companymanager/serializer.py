from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as CompanyModels
from usermanager import models as usermodel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModels.Company
        fields = '__all__'


    def create(self, validated_data):
         
        organization = CompanyModels.Company.objects.create(**validated_data)        
        userDAta = User.objects.create_user_company("vedasankoju@gmail.com", 'veda@123', organization)      
        return organization
 
