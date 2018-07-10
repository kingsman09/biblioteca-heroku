from django.urls import path
from . import views

app_name = 'prestamos'

urlpatterns = [
    path('lista', views.PrestamoOfUser, name='prestamos-list'),
    path('pre-prestamo/<int:pk>', views.PrestarLibroView.as_view(), name='pre-prestamo'),
   
]