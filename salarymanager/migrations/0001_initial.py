# Generated by Django 3.2.4 on 2023-06-16 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employeemanager', '0001_initial'),
        ('companymanager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='salaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sal_status', models.CharField(default=1, max_length=100)),
                ('updated_date', models.CharField(default='', max_length=100)),
                ('BasicSalary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('DearnessAllowance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('HouseRentAllowance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ConveyanceAllowance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('MedicalAllowance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('SpecialAllowance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('EmployeeProvidentFund', models.DecimalField(decimal_places=2, max_digits=6)),
                ('TaxDeductedatSource', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Professionaltax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companymanager.company')),
                ('employee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeemanager.employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
