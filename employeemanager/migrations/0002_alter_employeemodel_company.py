# Generated by Django 3.2.4 on 2023-09-01 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companymanager', '0001_initial'),
        ('employeemanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyEmploye', to='companymanager.company'),
        ),
    ]
