from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

CustomUser = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    address = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True,
                           widget=forms.HiddenInput())
    county = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(
        max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(
        max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(
        max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(
        max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ('address', 'town', 'county', 'post_code',
                  'country', 'longitude', 'latitude')


class CustomUserSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
    name = forms.CharField(max_length=30, required=True,
                           widget=forms.TextInput(attrs={'placeholder': '*Your name..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password Confirm..', 'class': 'password'}))
    # reCAPTCHA token
    token = forms.CharField(
        widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2')
