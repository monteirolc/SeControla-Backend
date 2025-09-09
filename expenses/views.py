from rest_framework import viewsets, permissions
from .models import Expense
from balance.models import Balance
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        expense = Expense.objects.filter(
            created_by=user,
            balance__account_type="e"
        )
        return expense

    def perform_create(self, serializer):
        user = self.request.user
        balance_id = self.request._data.get("balance")  # type: ignore
        balance = Balance.objects.filter(
            id=int(balance_id), account_type='e').first()
        if not balance:
            raise ValueError("No expense balance found for the user")
        serializer.save(
            balance=balance,
            created_by=user)
