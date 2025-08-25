from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "name", "last_name", "email", "cpf", "phone",
                    "age", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informações Pessoais", {"fields": ("name", "last_name", "age",
                                             "cpf", "email", "phone")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "is_superuser",
                                   "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "name", "last_name", "age", "cpf", "email",
                       "phone", "password1", "password2", "is_staff",
                       "is_active")}
         ),
    )

    search_fields = ("username", "email", "cpf", "name", "last_name")
    ordering = ("username",)
