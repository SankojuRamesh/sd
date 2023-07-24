from django.db import models
from companymanager.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime

from employeemanager.models import EmployeeModel




# Create your models here.



class AttendanceModel(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    company     = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_code   = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE) 
    sal_status      = models.CharField(max_length=100, default=1)
    created_date    = models.DateTimeField(default=datetime.now, blank=True)
    total_days      = models.IntegerField()
    attendance_days  = models.IntegerField()
    month = models.CharField(max_length=100, default=1)
    year = models.CharField(max_length=100, default=1)
    