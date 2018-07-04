from django.contrib import admin
from .models import Temas

# Register your models here.
class Theme(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso',)


admin.site.register(Temas, Theme)