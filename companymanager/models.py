from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    companycode = models.CharField(max_length=100, default='')
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='comapanydocs/', default='logo/freelogo.png')
    pf_persentage = models.CharField(max_length=12, null=True, blank=True, default='12')
    esi_persentage = models.CharField(max_length=12, null=True, blank=True, default='12')

    def __str__(self):
        return self.name
    
    @property
    def total_empolyes(self): 
        
        return  Company.objects.get(id=self.id).companyEmploye.all().count()




class NotificatonsModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    commapy = models.ForeignKey(Company, on_delete=models.CASCADE)
    stard_datae =  models.CharField(max_length=200, null=True, blank=True)
    end_datae =  models.CharField(max_length=200, null=True, blank=True)
    images_one = models.ImageField(upload_to='notifications/', null=True, blank=True)
    images_two = models.ImageField(upload_to='notifications/', null=True, blank=True)



    
