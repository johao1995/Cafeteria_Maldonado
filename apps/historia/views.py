from typing import List
from django.shortcuts import render
from .models import History
from django.views.generic import (
    ListView
)

class ListHistory(ListView):
    template_name='history/historia.html'

    def get_queryset(self):
        history=History.objects.lista_historias
        return history
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='History'
        context['historia']=self.get_queryset()
        return context
