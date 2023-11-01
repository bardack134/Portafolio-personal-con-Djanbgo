from django.shortcuts import render

from .models import InfoProyectos

# Create your views here.
def proyectos(request):
    # Obtenemos todos los objetos de la clase 'InfoProyectos' de la base de datos y los almacenamos en informacion
    informacion = InfoProyectos.objects.all() 

    contexto = {
        'informacion': informacion,
    }

    return render(request, 'projectos/proyectos.html', contexto)