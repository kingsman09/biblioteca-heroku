from django import forms

from .models import Libros

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = (
            'titulo',
            'autor',
            'tema',
            'biblioteca',
            'ubicacion',
            'disponibles',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({
            'class': 'form-control',
            })


