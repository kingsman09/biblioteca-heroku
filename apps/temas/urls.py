from django.urls import path
from . import views

app_name = 'temas'

urlpatterns = [
    path('crear-temas/', views.NewThemeView.as_view(), name='crear-tema'),
    path('temas-admin/', views.ThemeAdminView.as_view(), name='temas-admin'),
    path('eliminar-tema/<int:pk>', views.DeleteThemeView.as_view(), name='eliminar-tema'),
    path('editar-tema<int:pk>/', views.UpdateThemeView.as_view(), name='editar-tema'),
    
]