from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from usuarios.mixins import AdminMixin, UserMixin
from .models import Libros
from apps.autores.views import AuthorUserView
from apps.autores.models import Author
from .forms import BookCreationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class AdminBookList(AdminMixin, ListView):
    model = Libros
    context_object_name = 'Libro'
    paginate_by = 5
    template_name_suffix = '_list_admin'
    queryset = Libros.objects.all()

    # def get_paginate_by(self, queryset):
    #     try:
    #         paginate_by = self.request.GET.get('paginate_by', 5)
    #         paginate_by = int(paginate_by)
    #     except ValueError:
    #         paginate_by = 5
    #     finally:
    #         return paginate_by


def _update_or_create(view):
    class View(AdminMixin, view):
        model = Libros
        form_class = BookCreationForm
        success_url = reverse_lazy('book:admin_index')
    return View

CreateBookView = _update_or_create(CreateView)
UpdateBookView = _update_or_create(UpdateView)

class DeleteBookView(DeleteView):
    model = Libros
    success_url = reverse_lazy('book:admin_index')


class UserBookList(UserMixin, ListView):
    model = Libros
    context_object_name = 'Libro'
    template_name = 'libros/user_list.html'




#     model = Libros
#     context_object_name = 'Name'
#     template_name_suffix = '_pruebas'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(*kwargs)
#         context['titulo'] = Libros.objects.filter(autor__nombre__exact='walter')
#         serial = serializers.serialize('json' , context)
#         return JsonResponse(serial)