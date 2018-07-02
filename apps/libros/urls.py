from django.urls import path
from . import views as local_views
from usuarios import views

app_name = 'book'

urlpatterns = [
    path('index-admin/', local_views.AdminBookList.as_view(), name='admin_index'),
    # path('main/', views.IndexView.as_view(), name='admin_dashboard')
    path('index-user/', local_views.UserBookList.as_view(), name='user_index')
]