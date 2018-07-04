from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

# Create your models here.
class Temas(models.Model):
    tema = models.CharField(_('tema'), max_length=200)
    fecha_ingreso = models.DateField(_('fecha_ingreso'), default=now())

    class Meta:
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.tema