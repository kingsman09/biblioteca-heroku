from django.db import models
from django.utils.crypto import get_random_string
from apps.libros.models import Libros
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from datetime import datetime, timedelta



# Create your models here.
class Prestamo(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.PROTECT)
    fecha_prestamo = models.DateField(_('fecha de prestamos'), default=datetime.now())
    fecha_devolucion = models.DateField(_('fecha de devolucion'), default=(datetime.now() + timedelta(days=8)))
    token = models.CharField(max_length=50, unique=True) 
    estado = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.usuario.first_name}: {self.libro.titulo}'

    def is_deadline(self):
        return now().date() > self.fecha_devolucion

    @property
    def deadline(self):
        hoy = now().date()
        devolucion = self.fecha_devolucion        
        diff = devolucion - hoy
        return diff.days
        