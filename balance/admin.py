from django.contrib import admin
from .models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "date", "total_incomes",
                    "total_expenses", "created_at")
    search_fields = ("name", "date", "owner")
    list_filter = ("created_at",)
    # filter_horizontal = ("shared_accounts",)
