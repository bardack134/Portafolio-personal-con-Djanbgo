# Importa el módulo de administración de Django
from django.contrib import admin

# Importa funciones y clases relacionadas con las URL de Django
from django.urls import path, include

# Importa la configuración global del proyecto Django desde settings.py
from django.conf import settings

# Importa la función 'static' para manejar archivos estáticos y multimedia
from django.conf.urls.static import static

# Lista de patrones de URL del proyecto
urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Incluye las URL de la aplicación 'home' usando el archivo urls.py de esa aplicación
    path('', include('home.urls')),

    # Incluye las URL de la aplicación 'Projects' usando el archivo urls.py de esa aplicación
    path('proyectos', include('projectos.urls')),
]

# Configuración para servir archivos estáticos y multimedia durante el desarrollo
if settings.DEBUG:
    # Agrega las URL para servir archivos multimedia (MEDIA_URL) usando la ruta del sistema de archivos especificada en MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
