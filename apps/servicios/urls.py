from django.urls import path
from . import views
servicios_urlpatterns=([
    path('list-servicio/',views.ListService.as_view(),name='list-servicio')
],'servicio')