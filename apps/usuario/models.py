from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    sexo_choices=(
        ('H','Hombre'),
        ('M','Mujer')
    )
    username=models.CharField(max_length=30,unique=True,blank=False,verbose_name='Usuario')
    email=models.EmailField(blank=False,verbose_name='Correo')
    first_name=models.CharField(max_length=30,blank=False,verbose_name='Nombres')
    last_name=models.CharField(max_length=30,blank=False,verbose_name='Apellidos')
    is_staff=models.BooleanField(default=False,verbose_name='Estado')
    sexo=models.CharField(max_length=1,choices=sexo_choices,verbose_name='Sexo')

    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=('email','sexo')
    
    class Meta:
        verbose_name_plural='usuario'
        db_table='usuario'
    
    def __str__(self):
        return self.username
