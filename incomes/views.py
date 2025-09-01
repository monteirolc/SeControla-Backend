from rest_framework import viewsets, permissions
from .models import Income
from .serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        income = Income.objects.filter(
            created_by=user,
            balance__account_type="i"
        )
        return income

    def perform_create(self, serializer):
        # Associa automaticamente ao balance principal do usuário
        serializer.save(balance=self.request.user.balance)
