from django.db import models

# Create your models here.
class InfoProyectos2(models.Model):
    imagen = models.ImageField(upload_to='proyectos', null=True, blank=True)

    titulo = models.CharField(max_length=100)

    github_link = models.URLField(max_length=200, null=True, blank=True)

    link_proyecto = models.URLField(max_length=200, null=True, blank=True)

    introduccion = models.TextField()

    herramientas = models.TextField()

    resultadosLogros = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'infoProyectos2'

        verbose_name="infoProyecto2"
    
    def __str__(self):
        return self.titulo