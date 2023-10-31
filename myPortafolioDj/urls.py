"""
URL configuration for myPortafolioDj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Importa la configuración global de tu proyecto Django
from django.conf import settings

# Importa la función 'static' para servir archivos estáticos como imágenes y hojas de estilo CSS, para que puedas ver cómo se ven en tu aplicación.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

     path('', include('home.urls')),
]
# Si el modo DEBUG está activado (entorno de desarrollo), 
# agrega las URL para servir archivos multimedia (MEDIA_URL)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)