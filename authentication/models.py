from os import access
from django.db import models

# Create your models here.

from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self,phone,name,password=None):
        if phone is None:
            raise TypeError('User should have a phone number')
        
        user = self.model(phone=phone,name=name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,phone,name,password=None):
        if phone is None:
            raise TypeError('User should have phone')
        
        user = self.create_user(phone,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username = None
    name = models.CharField(max_length=225,unique=True,db_index=True)
    phone = models.CharField(max_length=225,unique=True,db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELD = ['name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.name
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        }