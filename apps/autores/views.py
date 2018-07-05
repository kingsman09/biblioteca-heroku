from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from .forms import AutorForm
from .models import Author

from usuarios.mixins import AdminMixin

# Create your views here.
class AuthorAdminView(AdminMixin, ListView):
    model = Author
    context_object_name = 'Autor'
    template_name_suffix = '_list_admin'


def _update_or_create(view):
    class View(AdminMixin, view):
        model = Author
        form_class = AutorForm
        success_url = reverse_lazy('autor:autores-admin')

    return View

NewAuthorView = _update_or_create(CreateView)
UpdateAuthorView = _update_or_create(UpdateView)


class DeleteAuthorView(AdminMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('autor:autores-admin')

