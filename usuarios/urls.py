from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='sign_out'),
    path('create-admin/', views.SignUpAdmin, name='sign_up_admin'),
    path('create-user/', views.SignUpUser, name='sign_up_user')
]