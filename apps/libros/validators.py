from django.core.exceptions import ValidationError


def limit(value):
    if value < 1:
        raise ValidationError('<li> ya no hay mas libros disponibles  </li>')
    

