from django.db import models

from companymanager.models import Company

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    pf_rate = models.DecimalField(max_digits=5, decimal_places=2)
    #suser = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
