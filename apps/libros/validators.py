from django.core.exceptions import ValidationError


def limit(value):
    if value < 1:
        raise ValidationError('Disponibilidad debe ser de al menos 1')
    

