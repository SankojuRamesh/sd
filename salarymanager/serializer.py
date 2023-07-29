from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as salaryModel
from usermanager import models as usermodel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class salaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = salaryModel.salaryModel
        fields = '__all__'

 

 