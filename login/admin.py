from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("login", "nome", "sobrenome", "email", "cpf", "telefone",
                    "idade", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("login", "password")}),
        ("Informações Pessoais", {"fields": ("nome", "sobrenome", "idade",
                                             "cpf", "email", "telefone")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "is_superuser",
                                   "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("login", "nome", "sobrenome", "idade", "cpf", "email",
                       "telefone", "password1", "password2", "is_staff",
                       "is_active")}
         ),
    )

    search_fields = ("login", "email", "cpf", "nome", "sobrenome")
    ordering = ("login",)
