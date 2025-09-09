from rest_framework import viewsets, permissions
from .models import Income
from .serializers import IncomeSerializer
from balance.models import Balance


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        income = Income.objects.filter(
            created_by=user,
            balance__account_type="i"
        )

        datei = self.request.query_params.get('datei')  # type: ignore
        datef = self.request.query_params.get('datef')  # type: ignore

        if datei and not datef:
            income = income.filter(
                created_at__gte=f'{datei} 00:00:00'
            )
        elif datef and not datei:
            income = income.filter(
                created_at__lte=f'{datef} 00:00:00'
            )
        elif datei and datef:
            income = income.filter(
                created_at__range=[f'{datei} 00:00:00', f'{datef} 00:00:00']
            )

        return income

    def perform_create(self, serializer):
        # Associa automaticamente ao balance principal do usuário
        user = self.request.user
        balance_id = self.request._data.get("balance")  # type: ignore
        print(self.request)
        balance = Balance.objects.filter(
            id=int(balance_id), account_type='i').first()
        if not balance:
            raise ValueError("No income balance found for the user.")
        serializer.save(
            balance=balance,
            created_by=user)
