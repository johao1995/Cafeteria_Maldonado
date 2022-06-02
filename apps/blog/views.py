import imp
from django.shortcuts import render
from .models import Blog
from django.views.generic import (
    ListView
)

class ListBlog(ListView):
    template_name='blog/blog.html'
    
    def get_queryset(self):
        blog=Blog.objects.lista_blogs
        return blog

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='BLog'
        context['blog']=self.get_queryset()
        return context