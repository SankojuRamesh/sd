from django.db import models
from companymanager.models import Company

from  employeemanager.models import  EmployeeModel

from django.contrib.auth import get_user_model
 
User = get_user_model()
# Create your models here.



class salaryModel(models.Model):
    # user         = models.ForeignKey(User, on_delete=models.CASCADE)
    company      = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_code   = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name="empsalary") 
    sal_status      = models.CharField(max_length=100, default=1, null=True, blank=True )
    updated_date   = models.CharField(max_length=100, default='', null=True, blank=True )
    BasicSalary    =models.CharField(max_length=20, null=True, blank=True )
    DearnessAllowance   =models.CharField(max_length=20 , null=True, blank=True )
    HouseRentAllowance  =models.CharField(max_length=20, null=True, blank=True  )
    ConveyanceAllowance =models.CharField(max_length=20,  null=True, blank=True )
    MedicalAllowance    =models.CharField(max_length=20,  null=True, blank=True )
    SpecialAllowance    =models.CharField(max_length=20,  null=True, blank=True )
    
    TaxDeductedatSource =models.CharField(max_length=20, null=True, blank=True )
    Professionaltax     =models.CharField(max_length=20,  null=True, blank=True )
    pf_deductiion =models.CharField(max_length=20,  null=True, blank=True )
    esi_deduction  = models.CharField(max_length=20, null=True, blank=True )
    netSal = models.CharField(max_length=20,  null=True, blank=True )
