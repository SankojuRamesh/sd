from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as CompanyModels


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModels.Company
        fields = '__all__'
        
