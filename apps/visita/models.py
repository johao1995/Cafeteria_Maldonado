from django.db import models
from .managers import VisitaManager

class Store(models.Model):
    dir=models.CharField(max_length=40,blank=False,verbose_name='Direccion')
    country=models.CharField(max_length=40,blank=False,verbose_name='Pais')
    phone=models.CharField(max_length=40,blank=False,verbose_name='Anexo')
    objects=VisitaManager()
    class Meta:
        verbose_name_plural='Store'
        db_table='store'
        ordering=('id',)
    
    def __str__(self):
        return self.dir
