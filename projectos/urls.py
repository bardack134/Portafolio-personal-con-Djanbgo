

from django.urls import path

from . import views


app_name='Projects'
# Define las URL de tu aplicación

urlpatterns = [
    path('', views.proyectos, name='proyectos'),
    
] 




