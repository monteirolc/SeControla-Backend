from django.contrib import admin
from .models import SharedAccount


@admin.register(SharedAccount)
class SheredAccountAdmin(admin.ModelAdmin):
    list_display = ("balance", "user", "role", "created_at")
    search_fields = ("balance__name", "user__username", "role")
    list_filter = ("role",)
