from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Balance
from .serializers import BalanceSerializer


class BalanceListView(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]  # só usuários logados

    def get(self):
        # só retorna o balance do usuário logado
        return Response(
            Balance.objects.filter(owner=self.request.user),
            status=status.HTTP_200_OK
        )
