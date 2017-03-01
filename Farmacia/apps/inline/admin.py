from django.contrib import admin
from models import *

class todolistAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(todo_list,todolistAdmin)