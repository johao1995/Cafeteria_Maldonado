from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomePage(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url=reverse_lazy('login')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Home'
        return context