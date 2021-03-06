from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from .models import Temas
from .forms import TemaForm
from django.urls import reverse_lazy
from apps.libros.models import Libros

from usuarios.mixins import AdminMixin, UserMixin

# Create your views here.
class ThemeAdminView(AdminMixin, ListView):
    model = Temas
    context_object_name = 'Temas'
    paginate_by = 5


def _update_or_create(view):
    class View(AdminMixin, view):
        model = Temas
        form_class = TemaForm
        success_url = reverse_lazy('temas:temas-admin')
    return View

NewThemeView = _update_or_create(CreateView)
UpdateThemeView = _update_or_create(UpdateView)
    
class DeleteThemeView(AdminMixin, DeleteView):
    model = Temas
    success_url = reverse_lazy('temas:temas-admin')


class ThemeUserView(UserMixin, ListView):
    model = Temas
    context_object_name = 'Temas'
    template_name_suffix = '_list_user'
    paginate_by = 5


def libro_tema(request, pk):
    books = Libros.objects.filter(tema__id=pk)
    context = {'Libros': books}
    return render(request, 'temas/libros_de_temas.html', context)