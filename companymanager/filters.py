# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Company, NotificatonsModel
import logging
from django_filters import rest_framework as filters

class CompanyFilter(filters.FilterSet):
    class Meta:
        model =Company
        fields =['id','email', 'phone']
class CompanynotificationFilter(filters.FilterSet):
    class Meta:
        model =NotificatonsModel
        fields =['id','commapy']
