from django.contrib import admin
from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Task, MainAdmin)
