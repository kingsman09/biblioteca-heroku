from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, View
from django.views.generic.edit import UpdateView
from usuarios.mixins import AdminMixin, UserMixin
from .models import Libros, Biblioteca
from apps.autores.views import AuthorUserView
from apps.autores.models import Author
from .forms import BookCreationForm
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# Create your views here.
class AdminBookList(AdminMixin,ListView):
    model = Libros
    context_object_name = 'Libro'
    paginate_by = 5
    
    template_name_suffix = '_list_admin'


    # def post(self, request):
    #     biblioteca = request.POST.get('biblio_id')
    #     return biblioteca
    
    # biblioteca1 = post

  

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
    # queryset = Libros.objects.filter(biblioteca_id=1)


class MostrarBibliotecas(ListView):
    model = Biblioteca
    context_object_name = 'Bibliotecas'
    template_name_suffix = '_list_bibliotecas'



class CrearBiblioteca(View):
    @staticmethod
    def get(request):
        return render(request, 'bibliotecas/crear_biblioteca.html')

    @staticmethod
    def post(request):
        data = request.POST
        Biblioteca.objects.create(
            nombre = data.get('nombre'),
            descripcion = data.get('descripcion'),
            ubicacion = data.get('ubicacion'),
            latitud = data.get('latitud'),
            longitud = data.get('longitud'),
            )

        return JsonResponse({"data": data})