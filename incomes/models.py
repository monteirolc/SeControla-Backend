# incomes/models.py
from django.db import models
from django.conf import settings


class Income(models.Model):
    balance = models.ForeignKey("balance.Balance", on_delete=models.CASCADE,
                                related_name="incomes")
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incomes_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount} ({self.created_by})"
