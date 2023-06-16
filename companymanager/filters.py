# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Company
import logging
from django_filters import rest_framework as filters

class CompanyFilter(filters.FilterSet):
    class Meta:
        model =Company
        fields =['email', 'phone']
