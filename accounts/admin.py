from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ( 'email', 'first_name', 'last_name', 'city', 'is_staff')

    


admin.site.register(CustomUser, CustomUserAdmin)
 