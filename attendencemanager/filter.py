# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import AttendanceModel
import logging
from django_filters import rest_framework as filters

class AttendanceFilter(filters.FilterSet):
    class Meta:
        model =AttendanceModel
        fields =['company', 'employee_code',"user"]