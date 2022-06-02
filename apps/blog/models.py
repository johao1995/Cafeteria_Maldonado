from django.db import models
from apps.servicios.models import Service
from .managers import BlogManager

class Blog(models.Model):
    fecha=models.DateField(max_length=40,blank=False,verbose_name='Fecha')
    title=models.CharField(max_length=40,blank=False,verbose_name='Titulo')
    servicio=models.ForeignKey(Service,on_delete=models.CASCADE,null=False,verbose_name='Servicio')
    description=models.CharField(max_length=30,blank=False,verbose_name='Descripcion')
    objects=BlogManager()

    class Meta:
        verbose_name_plural='Blog'
        db_table='blog'
        ordering=('id',)
    
    def __str__(self):
        return self.title
