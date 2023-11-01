from django.db import models

# Create your models here.
class infoProyectos(models.Model):
    titulo = models.CharField(max_length=100)

    github_link = models.URLField(max_length=200)

    introduccion = models.TextField()

    herramientas = models.TextField()

    resultadosLogros = models.TextField()

    class Meta:
        verbose_name_plural = 'infoProyectos'

        verbose_name="infoProyecto"
    
    def __str__(self):
        return self.titulo