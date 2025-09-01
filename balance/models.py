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
    ], default="i", blank=False, null=False)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_expenses(self):
        from expenses.models import Expense
        # from fixed_expenses.models import FixedExpense
        total_eventuais = Expense.objects.filter(balance=self).aggregate(
            models.Sum("amount"))["amount__sum"] or 0
        # total_fixos = FixedExpense.objects.filter(balance=self).aggregate(
        #     models.Sum("amount"))["amount__sum"] or 0
        return total_eventuais  # + total_fixos

    def total_incomes(self):
        from incomes.models import Income
        return Income.objects.filter(balance=self).aggregate(
            models.Sum("amount"))["amount__sum"] or 0

    @property
    def balance(self):
        return self.total_incomes() - self.total_expenses()

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
