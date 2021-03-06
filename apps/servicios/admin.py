from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'subtitle',
        'description',
        'image'
    )
admin.site.register(Service,ServiceAdmin)