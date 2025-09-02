from django.db import models
from django.conf import settings


class SharedAccount(models.Model):
    balance = models.ForeignKey(
        "balance.Balance",
        on_delete=models.CASCADE,
        related_name="shared_accounts"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shared_balances"
    )
    role = models.CharField(
        max_length=50,
        choices=[
            ("viewer", "Viewer"),       # só pode ver
            ("editor", "Editor"),       # pode editar
        ],
        default="viewer"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("balance", "user")  # evita duplicidade de acesso

    def __str__(self):
        return f"{self.user.username} → {self.balance.name} ({self.role})"