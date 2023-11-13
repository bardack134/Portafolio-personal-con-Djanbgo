from django.contrib import admin
from .models import InfoProyectos2

class InfoProyectos2Admin(admin.ModelAdmin):
    list_display = ('titulo', 'created', 'updated', 'introduccion')
    readonly_fields = ('created', 'updated')

admin.site.register(InfoProyectos2, InfoProyectos2Admin)

