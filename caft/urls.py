"""caft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.usuario import views
from .settings import local
from apps.home.urls import home_urlpatterns
from apps.historia.urls import historia_urlpatterns
from apps.servicios.urls import servicios_urlpatterns
from apps.visita.urls import visita_urlpatterns
from apps.contacto.urls import contacto_urlpatterns
from apps.blog.urls import blogs_urlpatterns

urlpatterns = [
    path('db-admin/', admin.site.urls),
    path('',views.UserLogin.as_view(),name='login'),
    path('logout/',views.UserLogout.as_view(),name='logout'),
    path('register/',views.UserRegister.as_view(),name='register'),
    path('home/',include(home_urlpatterns)),
    path('history/',include(historia_urlpatterns)),
    path('servicio/',include(servicios_urlpatterns)),
    path('visita/',include(visita_urlpatterns)),
    path('contacto/',include(contacto_urlpatterns)),
    path('blog/',include(blogs_urlpatterns))

]

if local.DEBUG==True:
    from django.conf.urls.static import static
    urlpatterns+=static(local.MEDIA_URL,document_root=local.MEDIA_ROOT)
