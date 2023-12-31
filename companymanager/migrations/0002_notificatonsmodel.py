# Generated by Django 3.2.4 on 2023-09-01 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companymanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificatonsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('stard_datae', models.CharField(blank=True, max_length=200, null=True)),
                ('end_datae', models.CharField(blank=True, max_length=200, null=True)),
                ('images_one', models.ImageField(blank=True, null=True, upload_to='notifications/')),
                ('images_two', models.ImageField(blank=True, null=True, upload_to='notifications/')),
                ('commapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companymanager.company')),
            ],
        ),
    ]
