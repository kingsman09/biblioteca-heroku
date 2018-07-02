from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Pais(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'paises'

    def __str__(self):
        return self.name

class Departamento(models.Model):
    pais = models.ForeignKey(Pais, verbose_name=_('Paises'), on_delete=models.CASCADE)
    name = models.CharField(_('Departamento'), max_length=150)

    class Meta:
        verbose_name_plural = 'departamentos'


    def __str__(self):
        return self.name

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, verbose_name=_('departamento'), on_delete=models.CASCADE)
    name = models.CharField(_('Municipio'), max_length=150)

    def __str__(self):
        return self.name