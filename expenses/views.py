from rest_framework import viewsets, permissions
from .models import Expense
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

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
