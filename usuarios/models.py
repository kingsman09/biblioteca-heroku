from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 
from django.core.validators import MaxValueValidator

from models.paises.models import Municipio
from models.paises.models import Departamento

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    adress = models.CharField(max_length=100 , null=True, blank=True)
    celphone = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(99999999)])
    gender = models.BooleanField(default=True, choices = [
        (True, 'Male'),
        (False, 'Female'),
    ])
    birth_date = models.DateField(blank=True, null=True)
    cui = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999999)])
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT,blank=True,  null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True)
    zona = models.PositiveIntegerField(_('zona del municipio'), blank=True, null=True)
    escolaridad = models.PositiveIntegerField(_('escolaridad'), default=0, choices=[
        ( 0, 'None' ),
        ( 1, 'Primaria'),
        ( 2,'Basicos'),
        ( 3, 'Diversificado'),
        ( 4, 'Universidad'),
        ( 5, 'Maestria'),
    ])
    establecimiento = models.CharField(_('establecimiento'), max_length=150, blank=True, null=True)
    estado = models.PositiveSmallIntegerField(_('estado'), default=1)
    imagen = models.ImageField(_('perfil'), upload_to='usuarios/avatares/', default='default_avatar.jpg', blank=True, null=True)

    def __str__(self):
        return self.get_full_name()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']
    

