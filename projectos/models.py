from django.db import models

# Create your models here.
class InfoProyectos(models.Model):
    imagen = models.ImageField(upload_to='proyectos')

    titulo = models.CharField(max_length=100)

    github_link = models.URLField(max_length=200)

    introduccion = models.TextField()

    herramientas = models.TextField()

    resultadosLogros = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'infoProyectos'

        verbose_name="infoProyecto"
    
    def __str__(self):
        return self.titulo