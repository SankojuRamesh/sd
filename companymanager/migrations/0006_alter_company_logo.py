# Generated by Django 3.2.4 on 2023-08-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companymanager', '0005_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='logo/freelogo.png', upload_to='comapanydocs/'),
        ),
    ]
