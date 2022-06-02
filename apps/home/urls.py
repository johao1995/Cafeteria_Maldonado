from django.urls import path
from . import views
home_urlpatterns=([
    path('',views.HomePage.as_view(),name='home-page')
],'home')