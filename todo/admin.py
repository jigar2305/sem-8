from django.contrib import admin
from todo.models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(status)
admin.site.register(bugdetail)
admin.site.register(Project_team)

