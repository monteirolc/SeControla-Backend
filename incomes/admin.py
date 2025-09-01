from django.contrib import admin
from .models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("balance", "description", "amount", "date",
                    "created_by", "created_at")
    search_fields = ("description", "balance__name", "created_by__username")
    list_filter = ("date", "created_by")
