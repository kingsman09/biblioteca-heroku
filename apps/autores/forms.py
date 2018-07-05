from django import forms
from .models import Author

class AutorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nombre', 'apellido', 'nacionalidad', 'genero', 'nacimiento', 'fallecimiento')
