from django.db import models
from django.conf import settings


class Balance(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="balances_owned"
    )
    name = models.CharField(max_length=100, default="Minha Planilha")
    account_type = models.CharField(max_length=20, choices=[
        ("i", "Receitas"),
        ("e", "Despesas"),
        ("fe", "Despesas Fixas"),
        ("fi", "Receitas Fixas"),
    ], default="i", blank=False, null=False)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_fixed_expenses(self):
        from fixed_expenses.models import FixedExpense
        fixed_expense_value = FixedExpense.objects.filter(
            balance=self).aggregate(
            models.Sum("amount"))["amount__sum"] or 0
        return fixed_expense_value

    def total_expenses(self):
        from expenses.models import Expense
        total_expenses_value = Expense.objects.filter(balance=self).aggregate(
            models.Sum("amount"))["amount__sum"] or 0
        return total_expenses_value

    def spending_sum(self):
        return self.total_fixed_expenses() + self.total_expenses()

    def total_incomes(self):
        from incomes.models import Income
        return Income.objects.filter(balance=self).aggregate(
            models.Sum("amount"))["amount__sum"] or 0

    def revenue_sum(self):
        return self.total_incomes()

    @property
    def balance(self):
        return self.revenue_sum() - self.spending_sum()

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
