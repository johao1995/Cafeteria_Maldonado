import re
from django.shortcuts import render
from .forms import ContactoForm
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)

class RegisterContacto(CreateView):
    template_name='contacto/register.html'
    form_class=ContactoForm
    success_url=reverse_lazy('contacto:register-contacto')