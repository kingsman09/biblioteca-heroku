from django.shortcuts import render, get_object_or_404, redirect
from usuarios.mixins import UserMixin, AdminMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Prestamo
from apps.libros.models import Libros
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def PrestamoOfUser(request):
    
    # template = loader.get_template('prestamos/')
    # paginator = Paginator(itemsquery, 10)
    # page = request.GET.get('page')
 
    # try:
    #     items = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     items = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     items= paginator.page(paginator.num_pages)

    prestamos = Prestamo.objects.filter(usuario=request.user)
    context = {'Prestamo': prestamos}
    return render(request, 'prestamos/prestamo_list.html', context)

class PrestarLibroView(UserMixin, DetailView):
    model = Libros
    template_name = 'prestamos/detalle_prestamo.html'

    def get_context_data(self, **kwargs):
        kwargs['fecha_prestamo'] = now()
        kwargs['fecha_devolucion'] = now() + timedelta(days=7)
        return super(PrestarLibroView, self).get_context_data(**kwargs)

    @staticmethod
    def post(request, *args, **kwargs):
        usuario_prestamo = Prestamo.objects.filter(usuario=request.user)
        print(len(usuario_prestamo))
        num = request.POST.get('book_id')
        usuario = request.user
        if usuario.estado != 2:
            if len(usuario_prestamo) < 10:
                libro = Libros.objects.get(pk=request.POST.get('book_id'))
                token = request.POST.get('token')
                Prestamo.objects.create(
                    libro=libro,
                    usuario=request.user,
                    token = token)
                libro.disponibles -= 1 
                libro.save()
                return redirect(reverse_lazy('book:user_index'))

            else:
                messages.error(request, 'Ha llegado a su limite de prestamos')
                return redirect(reverse_lazy('prestamos:pre-prestamo', kwargs={'pk': num}))
        else:       
            messages.error(request, 'No puede prestar por su estado Moroso')
            return redirect(reverse_lazy('prestamos:pre-prestamo', kwargs={'pk': num}))

    
class PrestamosAdminView(AdminMixin, ListView):
    model = Prestamo
    context_object_name = 'Prestamo'
    template_name_suffix = '_list_admin' 
    paginate_by = 5



def devolver_libro(request, pk):
    prestamo = Prestamo.objects.get(pk=pk)

    prestamo.estado = 3
    prestamo.save()
    prestamo.usuario.estado = 1
    prestamo.usuario.save()

    id_libro = prestamo.libro.id
    Libro = Libros.objects.get(id=id_libro)
    Libro.disponibles += 1
    Libro.save()

    
    
    return redirect(reverse_lazy('book:user_index'))
    
