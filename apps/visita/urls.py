from django.urls import path
from . import views
visita_urlpatterns=([
    path('list-visita/',views.ListStore.as_view(),name='list-visita')
],'visita')