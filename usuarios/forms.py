from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'celphone',
            'gender',
            'cui',
            'departamento',
            'municipio',
            'adress',
            'birth_date',
            'escolaridad',
            'establecimiento',
            'zona',
            'imagen'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control'})

class DetailForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'celphone',
            'gender',
            'cui',
            'departamento',
            'municipio',
            'adress',
            'birth_date',
            'escolaridad',
            'establecimiento',
            'zona',
            'imagen'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control'})

