from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/profile.html'
    login_url = 'accounts_login'


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'user'
    login_url = 'accounts_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return CustomUser.objects.filter(
            city__icontains=query,
        )
