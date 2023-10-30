

from django.urls import path

from . import views


app_name='Home'
# Define las URL de tu aplicación
urlpatterns = [
    path('', views.home, name='home'),
    
]




