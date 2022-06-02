
from django.shortcuts import render
from .models import Service
from django.views.generic import (
    ListView
)

class ListService(ListView):
    template_name='servicio/servicio.html'

    def get_queryset(self):
        service=Service.objects.lista_servicios
        return service
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Services'
        context['servicio']=self.get_queryset()
        return context
