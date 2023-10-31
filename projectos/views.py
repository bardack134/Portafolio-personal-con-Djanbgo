from django.shortcuts import render

# Create your views here.
def proyectos(request):

    return render(request, 'projectos/proyectos.html')