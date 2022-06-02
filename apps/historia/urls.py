from django.urls import path
from . import views
historia_urlpatterns=([
    path('list-history/',views.ListHistory.as_view(),name='list-history')
],'history')