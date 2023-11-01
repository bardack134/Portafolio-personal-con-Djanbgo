from django.contrib import admin

from .models import InfoProyectos
# Register your models here.

class InfoProyectosAdmin(admin.ModelAdmin):
         

     list_display = ('titulo', 'created', 'updated')

     list_editable = ('titulo',)

     #estos campos habiamos determinado que se actualizarian automaticamente, por lo tanto seran solo Lectura 
     readonly_fields=('created', 'updated')


admin.site.register(InfoProyectos, InfoProyectosAdmin)