from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 

from models.paises.models import Municipio
from models.paises.models import Departamento

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    celphone = models.PositiveIntegerField(blank=True, null=True)
    gender = models.BooleanField(default=True, choices = [
        (True, 'Male'),
        (False, 'Female'),
    ])
    birth_date = models.DateField(blank=True, null=True)
    cui = models.PositiveIntegerField(blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
    zona = models.PositiveIntegerField(_('zona del municipio'), null=True)
    escolaridad = models.PositiveIntegerField(_('escolaridad'), default=0, choices=[
        ( 1, 'None' ),
        ( 2, 'Primaria'),
        ( 3,'Basicos'),
        ( 4, 'Diversificado'),
        ( 5, 'Universidad'),
        ( 6, 'Maestria'),
    ])
    establecimiento = models.CharField(_('establecimiento'), max_length=150, null=True, blank=True)
    estado = models.PositiveSmallIntegerField(_('estado'), default=1)
    imagen = models.ImageField(_('perfil'), upload_to='usuarios/avatares/', default='default_avatar.jpg', blank=True, null=True)

    def __str__(self):
        return self.get_full_name()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']