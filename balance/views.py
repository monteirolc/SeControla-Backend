from rest_framework import viewsets, permissions, status
from django.db.models import Q
from .models import Balance
from .serializers import BalanceSerializer
from rest_framework.response import Response


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # O usuário só pode ver balances dele OU compartilhados com ele
        user = self.request.user
        balance = Balance.objects.filter(
            Q(owner=user) | Q(shared_accounts__user=user)).distinct()

        datei = self.request.query_params.get('datei')  # type: ignore
        datef = self.request.query_params.get('datef')  # type: ignore
        id = self.request.query_params.get('id')  # type: ignore

        if id:
            balance = balance.filter(id=id)

        if datei and datef:
            balance = balance.filter(date__range=[datei, datef])

        elif datei and not datef:
            balance = balance.filter(created_at__gte=datei)

        elif datef and not datei:
            balance = balance.filter(created_at__lte=datef)
        return balance

    def perform_create(self, serializer):
        # Ao criar, o balance é sempre associado ao usuário logado
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        id = self.request.data.get("id")  # type: ignore
        balance = Balance.objects.get(id=id)
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
