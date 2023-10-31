

from django.urls import path

from . import views

# Importa la configuración global de tu proyecto Django
from django.conf import settings

# Importa la función 'static' para servir archivos estáticos como imágenes y hojas de estilo CSS, para que puedas ver cómo se ven en tu aplicación.
from django.conf.urls.static import static

app_name='Home'
# Define las URL de tu aplicación
urlpatterns = [
    path('', views.home, name='home'),
    
]




