from django.shortcuts import render
from django.views.generic import TemplateView
from usuarios.mixins import AdminMixin, UserMixin

# Create your views here.
class AdminBookList(AdminMixin, TemplateView):
    template_name = 'libros/admin_list.html'


class UserBookList(UserMixin, TemplateView):
    template_name = 'libros/user_list.html'