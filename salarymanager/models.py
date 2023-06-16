from django.db import models
from companymanager.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()

from employeemanager.models import Employee

# Create your models here.



class salaryModel(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id      = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_code   = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    sal_status      = models.CharField(max_length=100, default=1)
    updated_date   = models.CharField(max_length=100, default='')
    BasicSalary    =models.DecimalField(max_digits=6, decimal_places=2)
    DearnessAllowance   =models.DecimalField(max_digits=6, decimal_places=2)
    HouseRentAllowance  =models.DecimalField(max_digits=6, decimal_places=2)
    ConveyanceAllowance =models.DecimalField(max_digits=6, decimal_places=2)
    MedicalAllowance    =models.DecimalField(max_digits=6, decimal_places=2)
    SpecialAllowance    =models.DecimalField(max_digits=6, decimal_places=2)
    EmployeeProvidentFund   =models.DecimalField(max_digits=6, decimal_places=2)
    TaxDeductedatSource =models.DecimalField(max_digits=6, decimal_places=2)
    Professionaltax     =models.DecimalField(max_digits=6, decimal_places=2)
