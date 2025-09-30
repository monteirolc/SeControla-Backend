from django.db import models
from django.conf import settings


class FixedIncome(models.Model):
    balance = models.ForeignKey("balance.Balance",
                                on_delete=models.CASCADE,
                                related_name="fixed_incomes")
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_day = models.PositiveSmallIntegerField()
    created_at = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True, blank=True
        )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def is_active_for_month(self, month_date):
        if not self.active:
            return False
        if self.start_date > month_date:
            return False
        if self.end_date and self.end_date < month_date:
            return False
        return True

    def __str__(self):
        return f"{self.description} - {self.amount}"


class FixedIncomeInstance(models.Model):
    fixed_income = models.ForeignKey(FixedIncome,
                                     on_delete=models.CASCADE,
                                     related_name="instances")
    balance = models.ForeignKey("balance.Balance",
                                on_delete=models.CASCADE,
                                related_name="fixed_expense_instances")
    reference_month = models.DateField()  # exemplo: 2025-08-01 para agosto/25
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.fixed_income.description} - \
                {self.reference_month.strftime('%m/%Y')} - {self.amount}")
