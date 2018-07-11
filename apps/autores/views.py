from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from .forms import AutorForm
from .models import Author
from apps.libros.models import Libros

from usuarios.mixins import AdminMixin, UserMixin

# Create your views here.
class AuthorAdminView(AdminMixin, ListView):
    model = Author
    context_object_name = 'Autor'
    template_name_suffix = '_list_admin'
    paginate_by = 5


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


class AuthorUserView(UserMixin, ListView):
    model = Author
    context_object_name = "Autor"
    template_name_suffix = '_list_user'
    paginate_by = 5



def books(request, pk):
    book = Libros.objects.filter(autor__id=pk)
    # book = book.objects.all()
    context = {'Book': book}
    return render(request, "autores/author_prueba.html", context)

