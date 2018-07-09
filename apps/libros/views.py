from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from usuarios.mixins import AdminMixin, UserMixin
from .models import Libros
from .forms import BookCreationForm
from django.urls import reverse_lazy

# Create your views here.
class AdminBookList(AdminMixin, ListView):
    model = Libros
    context_object_name = 'Libro'
    
    template_name_suffix = '_list_admin'
    queryset = Libros.objects.all()

    def get_paginate_by(self, queryset):
        try:
            paginate_by = self.request.GET.get('paginate_by', 5)
            paginate_by = int(paginate_by)
        except ValueError:
            paginate_by = 5
        finally:
            return paginate_by


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


class UserBookList(UserMixin, TemplateView):
    template_name = 'libros/user_list.html'