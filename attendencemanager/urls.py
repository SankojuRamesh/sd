# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'attendance', views.EmployeeAttendance, basename='attendanceViewSet')
router.register(r'newttendance', views.AttendanceViewSet, basename='newattendanceViewSet')
urlpatterns = [path(r'', include(router.urls))]
urlpatterns += []