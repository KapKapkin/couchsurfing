from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _



CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = ('email', 'name', 'town', 'is_staff')
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email", "town", "about_me", "avatar",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    


admin.site.register(CustomUser, CustomUserAdmin)
 