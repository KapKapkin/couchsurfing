from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm

CustomUser = get_user_model()

class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/profile.html'
    login_url = 'account_login'


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'user'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return CustomUser.objects.filter(
            city__icontains=query,
        )

class UserChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'account/change.html'
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        super(UserChangeView, self).post(request, *args, **kwargs)
        return redirect(request.user.get_absolute_url())



