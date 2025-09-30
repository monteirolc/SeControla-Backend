from django.contrib import admin
from .models import FixedIncome, FixedIncomeInstance


@admin.register(FixedIncome)
class FixedExpenseAdmin(admin.ModelAdmin):
    list_display = ('balance', 'description', 'amount', 'due_day',
                    'start_date', 'end_date', 'active')
    search_fields = ('name',)


@admin.register(FixedIncomeInstance)
class FixedExpenseInstanceAdmin(admin.ModelAdmin):
    list_display = ('fixed_income', 'balance', 'amount')
    search_fields = ('fixed_income__description',)
