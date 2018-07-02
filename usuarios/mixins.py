from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group

def _user_mixin(group_name):
    class Mixin(LoginRequiredMixin, UserPassesTestMixin):
        login_url = reverse_lazy('usuarios:index')

        def test_func(self):
            user = self.request.user

            if user.is_superuser:
                return True
        
            group = Group.objects.get(name=group_name)
            return group in user.groups.all()

    return Mixin

AdminMixin = _user_mixin('admin')
UserMixin = _user_mixin('user')