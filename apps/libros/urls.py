from django.urls import path
from . import views as local_views
from usuarios import views

app_name = 'book'

urlpatterns = [
    path('index-admin/', local_views.AdminBookList.as_view(), name='admin_index'),
    path('index-user/', local_views.UserBookList.as_view(), name='user_index'),

    path('crear-libro/', local_views.CreateBookView.as_view(), name='crear-libro'),
    path('editar-libro<int:pk>/', local_views.UpdateBookView.as_view(), name='editar-libro'),
    path('eliminar-libro<int:pk>', local_views.DeleteBookView.as_view(), name='eliminar-libro'),

    # path('pruebas/', local_views.BookOfAuthorView.as_view(), name='prueba')
]