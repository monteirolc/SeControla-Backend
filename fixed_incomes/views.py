from rest_framework import viewsets, permissions, status
from .serializers import FixedIncomeSerializer, FixedIncomeInstanceSerializer
from .models import FixedIncome, FixedIncomeInstance
from balance.models import Balance
from rest_framework.response import Response


class FixedIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = FixedIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        fixed_income = FixedIncome.objects.filter(
            created_by=user,
            balance__account_type="fe"
        )

        datei = self.request.query_params.get('datei')  # type: ignore
        datef = self.request.query_params.get('datef')  # type: ignore

        if datei and not datef:
            fixed_income = fixed_income.filter(
                created_at__gte=f'{datei} 00:00:00'
            )
        elif datef and not datei:
            fixed_income = fixed_income.filter(
                created_at__lte=f'{datef} 00:00:00'
            )
        elif datei and datef:
            fixed_income = fixed_income.filter(
                created_at__range=[f'{datei} 00:00:00', f'{datef} 00:00:00']
            )
        return fixed_income

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


class FixedIncomeInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = FixedIncomeInstanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FixedIncomeInstance.objects.filter(
            created_by=user,
            fixed_income__balance__account_type="fe"
        )

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
