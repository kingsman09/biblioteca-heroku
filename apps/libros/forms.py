from django import forms

from .models import Libros

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = (
            'titulo',
            'autor',
            'tema',
            'ubicacion',
            'disponibles',
        )
