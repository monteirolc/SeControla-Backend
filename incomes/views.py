from rest_framework import viewsets, permissions
from .models import Income
from .serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os incomes do balance do usuário logado
        return Income.objects.filter(balance__user=self.request.user)

    def perform_create(self, serializer):
        # Associa automaticamente ao balance principal do usuário
        serializer.save(balance=self.request.user.balance)
