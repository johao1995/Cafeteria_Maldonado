from unicodedata import name
from django.db import models

class Contacto(models.Model):
    name=models.CharField(max_length=40,blank=False,verbose_name='Nombre')
    email=models.EmailField(max_length=40,blank=False,verbose_name='Email')
    message=models.TextField(blank=False,verbose_name='Mensaje')

    class Meta:
        verbose_name_plural='Contacto'
        db_table='contact'
        ordering=('id',)
        
    def __str__(self):
        return self.name
