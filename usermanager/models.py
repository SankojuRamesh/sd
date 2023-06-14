# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import models as auth_models
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from . import managers


class User(auth_models.AbstractBaseUser, models.Model):
    """Custom user model that supports using email instead of username"""

    name = models.CharField(max_length=64)

    email = models.EmailField(max_length=64, unique=True)

    address = models.CharField(max_length=100, blank=True, null=True)

    contact = models.CharField(max_length=100, blank=True, null=True)

    #avatar = models.ImageField(_('Avatar'), upload_to=helper.avatar_path, blank=True, null=True)

    roles = models.ForeignKey('UserRole', blank=True, null=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'

    @property
    def get_roles(self):
        if self.roles:
            return self.roles.name


class UserRole(models.Model):
    "Model for handling user role"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('User Role')
        verbose_name_plural = _('User Roles')
