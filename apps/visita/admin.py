from django.contrib import admin
from .models import Store
class StoreAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'dir',
        'country',
        'phone',
    )
admin.site.register(Store,StoreAdmin)