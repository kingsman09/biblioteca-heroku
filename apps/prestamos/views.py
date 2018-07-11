from django.shortcuts import render, get_object_or_404, redirect
from usuarios.mixins import UserMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Prestamo
from apps.libros.models import Libros
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# Create your views here.
def PrestamoOfUser(request):
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
            raise ValidationError('Llego a su limite')


    # defget(self, request, pk):
    #     libro = get_object_or_404(Libros, pk=pk)
    #     Prestamo.usuario = request.user
    #     context = {'Libros': libro, 'Usuario': Prestamo.usuario}
    #     return render(request, 'prestamos/detalle_prestamo.html', context)
