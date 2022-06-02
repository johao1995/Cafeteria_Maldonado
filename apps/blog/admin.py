from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'fecha',
        'title',
        'servicio',
        'description',
        
    )
admin.site.register(Blog,BlogAdmin)