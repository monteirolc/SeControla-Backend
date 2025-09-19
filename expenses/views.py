from rest_framework import viewsets, permissions, status
from .models import Expense
from balance.models import Balance
from .serializers import ExpenseSerializer
from rest_framework.response import Response


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        expense = Expense.objects.filter(
            created_by=user,
            balance__account_type="e"
        )

        datei = self.request.query_params.get('datei')  # type: ignore
        datef = self.request.query_params.get('datef')  # type: ignore
        id = self.request.query_params.get('id')  # type: ignore

        if id:
            expense = expense.filter(id=id)

        if datei and datef:
            expense = expense.filter(date__range=[datei, datef])

        elif datei and not datef:
            expense = expense.filter(created_at__gte=datei)

        elif datef and not datei:
            expense = expense.filter(created_at__lte=datef)
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

    def perform_update(self, serializer):
        balance_id = self.request.data.get("balance")  # type: ignore
        balance = Balance.objects.get(id=balance_id)
        serializer.save(created_by=self.request.user, balance=balance)

    def update(self, request, *args, **kwargs):
        # AQUI, você busca o objeto e passa o campo que falta
        instance = self.get_object()
        data = request.data.copy()
        data['date'] = (
            f'{data['date'][6:10]}-{data['date'][3:5]}-{data['date'][0:2]}')
        # Agora, chame o serializer com os dados completos e o 'partial'
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
