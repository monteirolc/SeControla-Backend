from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Balance
from .serializers import BalanceSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # O usuário só pode ver balances dele OU compartilhados com ele
        user = self.request.user
        return Balance.objects.filter(
            Q(owner=user) | Q(shared_accounts__user=user)).distinct()

    def perform_create(self, serializer):
        # Ao criar, o balance é sempre associado ao usuário logado
        serializer.save(owner=self.request.user)
