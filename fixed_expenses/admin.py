from django.contrib import admin
from .models import FixedExpense, FixedExpenseInstance


@admin.register(FixedExpense)
class FixedExpenseAdmin(admin.ModelAdmin):
    list_display = ('balance', 'description', 'amount', 'due_day',
                    'start_date', 'end_date', 'active')
    search_fields = ('name',)


@admin.register(FixedExpenseInstance)
class FixedExpenseInstanceAdmin(admin.ModelAdmin):
    list_display = ('fixed_expense', 'balance', 'amount')
    search_fields = ('fixed_expense__description',)
