from django.contrib import admin
from .models import SharedAccount


@admin.register(SharedAccount)
class SharedAccountAdmin(admin.ModelAdmin):
    list_display = ("balance", "user", "name", "role", "first_name_shared",
                    "created_at")
    search_fields = ("balance__name", "user__username", "first_name_shared",
                     "role")
    list_filter = ("role",)
