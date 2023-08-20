from django.db import models

from companymanager.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()
# from salarymanager.serializer import salaryModelSerializer
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
 
 
User = get_user_model()

# Create your models here.
class EmployeeModel(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    company         = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100, default='', null=True, blank=True)
    phone         = models.CharField(max_length=100, default='', null=True, blank=True)
    husband_Father  = models.CharField(max_length=100, default='', null=True, blank=True)
    designation     = models.CharField(max_length=100, default='', null=True, blank=True)
    relation_name   = models.CharField(max_length=100, default='', null=True, blank=True)
    employee_code   = models.CharField(max_length=100, default='', null=True, blank=True)
    gender          = models.CharField(max_length=100, default='', null=True, blank=True)
    blood_group     = models.CharField(max_length=100, default='', null=True, blank=True)
    contact_number  = models.CharField(max_length=100, default='', null=True, blank=True)
    dob             = models.CharField(max_length=100, default='', null=True, blank=True)
    date_of_joining = models.CharField(max_length=100, default='', null=True, blank=True)
    email           = models.CharField(max_length=100, default='', null=True, blank=True)
    aadhar_number   = models.CharField(max_length=100, default='', null=True, blank=True)
    uan_number      = models.CharField(max_length=100, default='', null=True, blank=True)
    pan_number      = models.CharField(max_length=100, default='', null=True, blank=True)    
   
    esi_no      = models.CharField(max_length=100, default='', null=True, blank=True)
    esi_account      = models.CharField(max_length=100, default='yes', null=True, blank=True)
    pf_no           = models.CharField(max_length=100, default='', null=True, blank=True)
    pf_account      = models.CharField(max_length=100, default='yes', null=True, blank=True)
    pf_date         = models.CharField(max_length=100, default='', null=True, blank=True)
    basic_salary    = models.CharField(max_length=100, default='', null=True, blank=True)
    bank_ac_no      = models.CharField(max_length=100, default='', null=True, blank=True)
    bank_name       = models.CharField(max_length=100, default='', null=True, blank=True)
    ifsc_code       = models.CharField(max_length=100, default='', null=True, blank=True)
    Image           = models.CharField(max_length=100, default='', null=True, blank=True) 

    def __str__(self):
        return self.first_name



class EmpFamaly(models.Model):
    emiid = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE) 
    name =  models.CharField(max_length=100, default='', null=True, blank=True)
    relation  =  models.CharField(max_length=100, default='', null=True, blank=True)
    age =    models.CharField(max_length=100, default='', null=True, blank=True)
    aadhar =    models.ImageField(upload_to='famaly/', default='', null=True, blank=True)
    photo =  models.ImageField(upload_to='famaly/', default='', null=True, blank=True)
    
 
@receiver(post_delete, sender=EmployeeModel)
def post_delete_callback(sender, instance, *args, **kwargs):
    try: 
        phone_number  = str(instance.phone)+str(instance.aadhar_number[-4]) 
        u = User.objects.get(phone = phone_number) 
        print( u.id)
        u.delete()
    except:
        print('')
     
    
    
    
