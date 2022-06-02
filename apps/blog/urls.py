from django.urls import path
from . import views

blogs_urlpatterns=([
    path('list-blog/',views.ListBlog.as_view(),name='list-blog')
],'blog')