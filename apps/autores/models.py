from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.temas.models import Temas
from models.paises.models import Pais
from django.utils.timezone import now


# Create your models here.

class Author(models.Model):
    nombre = models.CharField(_('nombre'), max_length=150)
    apellido = models.CharField(_('apellido'), max_length=150)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)
    genero = models.BooleanField(_('genero'), default=True, choices=[
        (True, 'masculino'),
        (False, 'femenino')
    ])
    nacimiento = models.DateField(_('fecha de nacimiento'))
    fallecimiento = models.DateField(_('fecha de fallecimiento'),null=True, blank=True)
    fecha_registro = models.DateField(_('fecha de registro'), default=now())

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


