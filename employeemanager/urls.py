# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import  DownloadViewSet

from . import views

router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet  )
router.register(r'employeefamaly', views.EmployeeFamalyViewSet  )

 

urlpatterns = [path(r'', include(router.urls))]

urlpatterns += []