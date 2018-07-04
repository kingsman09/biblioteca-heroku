from django.contrib import admin
from .models import Author


# Register your models here.
class Autor(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)


admin.site.register(Author, Autor)