from django.contrib import admin
from .models import Libros

# Register your models here.

class Book(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)

admin.site.register(Libros, Book)
