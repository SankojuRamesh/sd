# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import EmployeeModel, EmpFamaly
import logging
from django_filters import rest_framework as filters

class employeeFilter(filters.FilterSet):
    class Meta:
        model =EmployeeModel
        fields =['company',  'aadhar_number','pf_no', 'addedby']



class employeeFamalyFilter(filters.FilterSet):
    class Meta:
        model =EmpFamaly
        fields =['id',  'emiid']