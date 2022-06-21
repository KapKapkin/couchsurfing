from allauth.account.forms import SignupForm
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'city', 'password')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'city', 'password')


class CustomUserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserSignupForm, self).__init__(*args, **kwargs)
        self.fields["first_name"] = forms.CharField(
            label='first name', max_length=100, required=False)
        self.fields["last_name"] = forms.CharField(
            label='last name', max_length=100, required=False)
        self.fields["city"] = forms.CharField(
            label='City', max_length=100, required=False)

    def save(self, request):
        user = super(CustomUserSignupForm, self).save(request)
        user.ifirst_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data["city"]
        user.save()
        return user
