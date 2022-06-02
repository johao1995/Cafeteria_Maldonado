
from django.shortcuts import render
from .models import Store
from django.views.generic import (
    ListView
)

class ListStore(ListView):
    template_name='store/store.html'

    def get_queryset(self):
        service=Store.objects.lista_visitas
        return service
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Store'
        context['visita']=self.get_queryset()
        return context
