from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(get_user_model())
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
         (None, {'fields': ('username', 'password', 'email')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'cui', 'birth_date', 'gender', 'celphone', 
                                         'adress',  'departamento', 'municipio','escolaridad', 'establecimiento','zona','imagen', 'estado')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )



