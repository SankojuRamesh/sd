from django.db import models

from companymanager.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Employee(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id      = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100, default='')
    husband_Father  = models.CharField(max_length=100, default='')
    designation     = models.CharField(max_length=100, default='')
    relation_name   = models.CharField(max_length=100, default='')
    employee_code   = models.CharField(max_length=100, default='')
    gender          = models.CharField(max_length=100, default='')
    blood_group     = models.CharField(max_length=100, default='')
    contact_number  = models.CharField(max_length=100, default='')
    dob             = models.CharField(max_length=100, default='')
    date_of_joining = models.CharField(max_length=100, default='')
    email           = models.CharField(max_length=100, default='')
    aadhar_number   = models.CharField(max_length=100, default='')
    uan_number      = models.CharField(max_length=100, default='')
    pan_number      = models.CharField(max_length=100, default='')
    pf_account      = models.CharField(max_length=100, default='yes')
    pf_no           = models.CharField(max_length=100, default='')
    pf_date         = models.CharField(max_length=100, default='')
    basic_salary    = models.CharField(max_length=100, default='')
    bank_ac_no      = models.CharField(max_length=100, default='')
    bank_name       = models.CharField(max_length=100, default='')
    ifsc_code       = models.CharField(max_length=100, default='')
    Image           = models.CharField(max_length=100, default='') 

    def __str__(self):
        return self.name
    

    
