from rest_framework import viewsets, permissions
from .models import SharedAccount
from .serializers import SharedAccountSerializer


class SharedAccountViewSet(viewsets.ModelViewSet):
    serializer_class = SharedAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Usuário vê apenas os compartilhamentos onde ele está envolvido
        return (
            SharedAccount.objects.filter(user=user) |
            SharedAccount.objects.filter(balance__owner=user)
        )

    def perform_create(self, serializer):
        """
        Ao criar um compartilhamento, o balance deve pertencer
        ao usuário logado.
        Isso garante que só o dono pode compartilhar.
        """
        balance = serializer.validated_data["balance"]
        if balance.owner != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "Você não pode compartilhar um balance que não é seu."
            )
        serializer.save()
