from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.views.generic import CreateView, View
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        user = request.user

        # if user.is_superuser:
        #     return redirect('/admin/')

        admin_user = Group.objects.get(name='admin')
        if admin_user in user.groups.all():
            return redirect(reverse_lazy('book:admin_index'))

        regular_user = Group.objects.get(name='user')
        if regular_user in user.groups.all():
            return redirect(reverse_lazy('book:user_index'))    


class SignInView(LoginView):
    template_name = 'usuarios/login.html'


def _sign_up(name):
    class SignUpView(CreateView):
        model = get_user_model()
        form_class = UserCreationForm
        success_url = reverse_lazy('usuarios:index')
        template_name = 'usuarios/user_form.html'

        def form_valid(self, form:UserCreationForm):
            user = form.save()
            user.groups.set([Group.objects.get(name=name)])

            if 'imagen' in self.request.FILES:
                user.imagen = self.request.FILES.get('imagen')

            # user.is_superuser = True
            user.save()

            return redirect(self.success_url)

    return SignUpView.as_view()

SignUpAdmin = _sign_up('admin')
SignUpUser = _sign_up('user')
        




class SignOutView(LoginRequiredMixin, LogoutView):
    pass
