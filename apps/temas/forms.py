from django import forms
from . import models

class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Temas
        fields = ('tema',)
