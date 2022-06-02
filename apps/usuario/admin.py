from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display=('id','username','is_staff','sexo')

admin.site.register(User,UserAdmin)