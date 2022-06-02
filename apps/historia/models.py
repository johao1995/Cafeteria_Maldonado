from django.db import models
from .managers import HistoryManager

class History(models.Model):
    title=models.CharField(max_length=40,blank=False,verbose_name='Titulo')
    subtitle=models.CharField(max_length=40,blank=False,verbose_name='SubTitulo')
    description=models.CharField(max_length=40,blank=False,verbose_name='Descripcion')
    image=models.ImageField(upload_to='media/historia/img',null=False,verbose_name='Imagen')

    objects=HistoryManager()

    class Meta:
        verbose_name_plural='Historia'
        db_table='history'
        ordering=('id',)
    
    def __str__(self):
        return self.title
