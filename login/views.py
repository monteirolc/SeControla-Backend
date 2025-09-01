from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginView(APIView):
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Pegando o usuário autenticado
        user = serializer.validated_data["user"]

        # Criando tokens
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Response(
            {
                "message": "Login successful",
                "refresh": str(refresh),
                "access": access,
            },
            status=status.HTTP_200_OK
        )
