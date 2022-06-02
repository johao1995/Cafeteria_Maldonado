from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'email',
        'message'
    )
admin.site.register(Contacto,ContactoAdmin)
