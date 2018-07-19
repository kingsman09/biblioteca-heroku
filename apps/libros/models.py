from django.db import models
from apps.temas.models import Temas
from apps.autores.models import Author
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .validators import limit




class Biblioteca(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)
    latitud = models.CharField(max_length=300)
    longitud = models.CharField(max_length=300)

    
    def __str__(self):
        return self.nombre

    
    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'


# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(_('titulo'), max_length=150)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.PROTECT, null=True)
    autor = models.ForeignKey(Author, on_delete=models.PROTECT)
    tema = models.ForeignKey(Temas, on_delete=models.PROTECT)
    ubicacion = models.CharField(_('ubicacion'), max_length=200)
    disponibles = models.PositiveIntegerField(_('libros disponibles'), validators=[limit], default=1, )
    fecha_registro = models.DateField(_('Fecha de ingreso'), default=now())

    class Meta: 
        ordering = ['id']
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'{self.titulo} - {self.autor}'