from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from models.paises.models import Pais
from apps.temas.models import Temas
from apps.libros import models as lm


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

    @property
    def books(self):
        return len(lm.Libros.objects.filter(autor__id=self.id))
