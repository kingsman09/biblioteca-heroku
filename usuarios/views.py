from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import UserCreationForm, DetailForm
from django.views.generic import CreateView, View, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from .mixins import AdminMixin, UserMixin
from .models import User
from apps.libros.models import Biblioteca


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        user = request.user

        if user.is_superuser:
            return redirect('/admin/')

        admin_user = Group.objects.get(name='admin')
        if admin_user in user.groups.all():
            return redirect(reverse_lazy('book:admin_index'))

        regular_user = Group.objects.get(name='user')
        if regular_user in user.groups.all():
            return redirect(reverse_lazy('book:user_index'))    




class SignInView(LoginView):
    
    
    @staticmethod
    def get(request):
        bibliotecas = Biblioteca.objects.all()
        return render(request, 'usuarios/login.html', {'bibliotecas':bibliotecas})

    # @staticmethod
    # def post(request):
    #     data = request.POST
    #     username = data.get('biblioteca')
    #     return JsonResponse({'biblioteca': username})

    template_name = 'usuarios/login.html'
        



        


def _sign_up(name):
    class SignUpView(CreateView):
        model = get_user_model()
        form_class = UserCreationForm
        success_url = reverse_lazy('usuarios:login')
        template_name = 'usuarios/create_user.html'

        def form_valid(self, form:UserCreationForm):
            if form.is_valid:
                user = form.save()
                user.groups.set([Group.objects.get(name=name)])

                if 'imagen' in self.request.FILES:
                    user.imagen = self.request.FILES.get('imagen')
       
                user.save()
                form.save()

            return redirect(self.success_url)

    return SignUpView.as_view()

SignUpAdmin = _sign_up('admin')
SignUpUser = _sign_up('user')
        

class SignOutView(LoginRequiredMixin, LogoutView):
    pass


class UserListView(AdminMixin, ListView):
    model = get_user_model() 
    queryset = model.objects.filter(groups__name__in=['user'])   
    context_object_name = 'Users'
    paginate_by = 5

class UserDetailView(AdminMixin, UpdateView):
    model = get_user_model()
    form_class = DetailForm
    success_url = 'usuarios:user-list'

class UserUpdateView(UserMixin, UpdateView):
    model = get_user_model()
    form_class = DetailForm
    success_url = reverse_lazy('book:user_index')
    template_name = 'usuarios/edit_user.html'

    def form_valid(self, form:UserCreationForm):
        if form.is_valid:
            user = form.save()
            
            if 'imagen' in self.request.FILES:
                user.imagen = self.request.FILES.get('imagen')

            user.save()
            form.save()

        return redirect(self.success_url)

    


    
