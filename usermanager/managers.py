# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from usermanager import models  as usermodel


class UserManager(auth_models.BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):

        "Creates and saves a new user"

        if not phone:
            raise ValueError(_('Users must have an email address'))

        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password):

        "Creates and saves a new superuser"

        user = self.create_user(phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    def create_user_company(self, phone, password , company, userType, name='admin_'):
        user = self.create_user(phone, password)        
        user.company = company        
        user.is_staff = True
        user.is_superuser = False
        user.is_admin = True
        user.name= name 
        roleid= 4
        if userType == 'Employee':
            roleid = 4
        user.roles = usermodel.UserRole.objects.get(id=roleid)
        user.save(using=self._db)
        return user

    def create_subadmin_company(self, phone, password , company, userType, name=''):
        user = self.create_user(phone, password)        
        user.company = company        
        user.is_staff = False
        user.is_superuser = False
        user.is_admin = True
        user.name= name
        roleid= 3
        if userType == 'SubAdmin':
            roleid = 3
        user.roles = usermodel.UserRole.objects.get(id=roleid)
        user.save(using=self._db)
        return user
