from django.db import models
from .managers import ServicioManager

class Service(models.Model):
    title=models.CharField(max_length=40,blank=False,verbose_name='Titulo')
    subtitle=models.CharField(max_length=40,blank=False,verbose_name='SubTitulo')
    description=models.CharField(max_length=40,blank=False,verbose_name='Descripcion')
    image=models.ImageField(upload_to='media/servicios/img',null=False,verbose_name='Imagen')
    objects=ServicioManager()
    
    class Meta:
        verbose_name_plural='Servicios'
        db_table='service'
        ordering=('id',)
    
    def __str__(self):
        return self.title
