# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'attendance', views.AttendanceViewSet, basename='attendanceViewSet')
urlpatterns = [path(r'', include(router.urls))]

urlpatterns += []