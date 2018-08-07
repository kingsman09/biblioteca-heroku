from django.urls import path
from . import views

app_name = 'prestamos'

urlpatterns = [
    path('lista', views.PrestamoOfUser, name='prestamos-list'),
    path('pre-prestamo/<int:pk>', views.PrestarLibroView.as_view(), name='pre-prestamo'),
    path('admin-list/', views.PrestamosAdminView.as_view(), name='prestamo-admin'),
    path('devolucion<int:pk>/ ', views.devolver_libro, name='devolver'),

    path('devolver-libro/', views.DevolverLibroView.as_view(), name='devolver-codigo'), 
   
]