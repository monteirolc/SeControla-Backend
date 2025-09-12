from rest_framework import viewsets, permissions
from .serializers import FixedExpenseSerializer, FixedExpenseInstanceSerializer
from .models import FixedExpense, FixedExpenseInstance
from balance.models import Balance


class FixedExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = FixedExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        fixed_expense = FixedExpense.objects.filter(
            created_by=user,
            balance__account_type="fe"
        )
        return fixed_expense

    def perform_create(self, serializer):
        user = self.request.user
        balance_id = self.request._data.get("balance")  # type: ignore
        balance = Balance.objects.filter(
            id=int(balance_id),
            account_type="fe"
        ).first()
        if not balance:
            raise ValueError("No balance to save")
        serializer.save(
            created_by=user,
            balance=balance
        )


class FixedExpenseInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = FixedExpenseInstanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FixedExpenseInstance.objects.filter(
            created_by=user,
            fixed_expense__balance__account_type="fe"
        )

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
