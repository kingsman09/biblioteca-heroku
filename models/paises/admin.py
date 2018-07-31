from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(models.Pais)
# admin.site.register(models.Departamento)
# admin.site.register(models.Municipio)

@admin.register(models.Pais)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(models.Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    pass

@admin.register(models.Municipio)
class MunicipioAdmin(ImportExportModelAdmin):
    pass