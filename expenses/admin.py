from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("balance", "description", "amount",
                    "date", "created_by", "created_at",
                    "updated_at")
    search_fields = ("created_by__username", "description", "date",
                     "amount")
    list_filter = ("created_at", "updated_at")
