# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Employee
import logging
from django_filters import rest_framework as filters

class employeeFilter(filters.FilterSet):
    class Meta:
        model =Employee
        fields =['company',  'aadhar_number','pf_no']