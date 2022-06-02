from django.urls import path
from . import views
contacto_urlpatterns=([
    path('register-contacto/',views.RegisterContacto.as_view(),name='register-contacto')
],'contacto')