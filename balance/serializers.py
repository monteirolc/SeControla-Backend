from rest_framework import serializers
from .models import Balance
from shared_accounts.serializers import SharedAccountSerializer


class BalanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.name")
    shared_accounts = SharedAccountSerializer(
        many=True,
        required=False,
        read_only=True
        )

    class Meta:
        model = Balance
        fields = ["id", "name",  "created_at", "total_incomes",
                  "total_expenses", "total_fixed_expenses", "account_type",
                  "balance", "owner", "shared_accounts"]
