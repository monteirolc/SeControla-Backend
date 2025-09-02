from rest_framework import viewsets, permissions
from .serializers import FixedExpenseSerializer, FixedExpenseInstanceSerializer
from .models import FixedExpense, FixedExpenseInstance


class FixedExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = FixedExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        fixed_expense = FixedExpense.objects.filter(
            createb_by=user,
            balance__account_type="fe"
        )
        return fixed_expense

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)


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
