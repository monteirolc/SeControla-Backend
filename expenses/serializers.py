from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["created_by", "updated_at", "created_at"]

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=False)

        if not valid:
            # Aqui você pode logar ou printar os erros
            print("⚠️ Erros de validação no ExpenseSerializer:")
            print(self.errors)

            # Ou, se quiser, levantar uma exceção mais descritiva
            if raise_exception:
                raise serializers.ValidationError(self.errors)

        return valid
