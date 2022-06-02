from django.urls import reverse_lazy
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from .forms import LoginForm,RegisterForm
from django.views.generic import (
    View,
    FormView
)


class UserLogin(FormView):
    template_name='usuario/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('home:home-page')

    def dispatch(self,request,*args,**kwargs):
        if request.method=="GET":
            if request.user.is_authenticated:
                return redirect('home:home-page')
        
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
       user=authenticate(
           username=form.cleaned_data['username'],
           password=form.cleaned_data['password']
       )
       print("**autenticando")
       print(user)
       login(self.request,user)
       return super().form_valid(form)

class UserLogout(View):

    def get(self,request):
        logout(request)
        return redirect('login')

class UserRegister(FormView):
    template_name='usuario/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('login')

    def form_valid(self,form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            form.cleaned_data['sexo'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        return super().form_valid(form) 