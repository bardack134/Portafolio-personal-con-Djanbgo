from django.shortcuts import render

from .models import InfoProyectos2

# Create your views here.
def proyectos(request):
    # Obtenemos todos los objetos de la clase 'InfoProyectos' de la base de datos y los almacenamos en informacion
    informacion = InfoProyectos2.objects.all() 

    contexto = {
        'informacion': informacion,
    }

    return render(request, 'projectos/proyectos.html', contexto)