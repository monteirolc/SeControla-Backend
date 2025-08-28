from django.contrib import admin
from .models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'created_at', 'date',
                    'total_expenses', 'total_incomes')
    search_fields = ('owner', 'created_at', 'date')
    list_filter = ('created_at', 'owner')

# Register your models here.
