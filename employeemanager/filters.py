# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import EmployeeModel
import logging
from django_filters import rest_framework as filters

class employeeFilter(filters.FilterSet):
    class Meta:
        model =EmployeeModel
        fields =['company',  'aadhar_number','pf_no']