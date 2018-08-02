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
import json
from usuarios.models import User

from apps.prestamos.models import Prestamo 
# Create your views here.

def fecha_limite():
    Prestamos = Prestamo.objects.all()

    for prestamo in Prestamos:
        if prestamo.deadline < 1:
            prestamo.estado = 2
            prestamo.usuario.estado = 2
            prestamo.save()
            prestamo.usuario.save()
        else:
            prestamo.estado = 1
            prestamo.usuario.estado = 1
            prestamo.save()
            prestamo.usuario.save()
            
    
    

class AdminBookList(AdminMixin,ListView):
    
    model = Libros
    context_object_name = 'Libro'
    paginate_by = 5
    template_name_suffix = '_list_admin'
    fecha_limite()
  

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



class UserBookList(UserMixin,View):
    
    fecha_limite()
    
    @staticmethod
    def get(request):
        biblioteca = Biblioteca.objects.all()
        return render(request, 'libros/user_list.html', {'Biblioteca': biblioteca})
    
    @staticmethod
    def post(request):
        data = request.POST
        
        nuevo = data.get('biblioteca_id')
        print(nuevo)
        libros = Libros.objects.filter(biblioteca__id = nuevo).values('id', "titulo", "autor__nombre", "tema__tema", "disponibles", "ubicacion", "fecha_registro")
        libros = json.dumps(list(libros), cls=serializers.json.DjangoJSONEncoder)
        
        return JsonResponse({"Libro": libros})
        

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

