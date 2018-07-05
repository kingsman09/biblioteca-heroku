from django.urls import path
from . import views


app_name = 'autor'

urlpatterns = [
    path('autores/', views.AuthorAdminView.as_view() ,name='autores-admin'),

    path('crear-autor/', views.NewAuthorView.as_view(), name='crear-autor'),
    path('editar-autor<int:pk>/', views.UpdateAuthorView.as_view(), name='editar-autor'),
    path('eliminar-autor<int:pk>/', views.DeleteAuthorView.as_view(), name='eliminar-autor')
]