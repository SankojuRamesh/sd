from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models as Attendance
from usermanager import models as usermodel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from employeemanager.serializer import EmployeeSerializer


User = get_user_model()  

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance.AttendanceModel
        fields = '__all__'

    



 