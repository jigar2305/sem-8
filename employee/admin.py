from django.contrib import admin
from .models import *


admin.site.register(role)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active", "phone_number","roleid","picture")
    list_display = ("username",  "email", "is_staff","role", "picture")
    list_filter =  ("is_staff",)
