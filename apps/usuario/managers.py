from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager,models.Manager):
    def _create_user(self,username,email,password,sexo,is_staff,is_superuser,**extra_fields):
        user=self.model(
            username=username,
            email=email,
            sexo=sexo,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,username,email,password,sexo,**extra_fields):
        return self._create_user(username,email,password,sexo,False,False,**extra_fields)
    
    def create_superuser(self,username,email,password,sexo,**extra_fields):
        return self._create_user(username,email,password,sexo,True,True,**extra_fields)