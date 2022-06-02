from django.contrib import admin
from .models import History
class HistoryAdmin(admin.ModelAdmin):
    list_display=('id','title','subtitle','description','image')
admin.site.register(History,HistoryAdmin)
