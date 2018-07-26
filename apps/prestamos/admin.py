from django.contrib import admin
from .models import Prestamo
# Register your models here.



class PrestamoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'usuario',
        'libro',
        'fecha_prestamo',
        'fecha_devolucion',
        'token',
        'estado',
        

    )

admin.site.register(Prestamo, PrestamoAdmin)
