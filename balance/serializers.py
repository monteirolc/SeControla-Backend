from rest_framework import serializers
from .models import Balance
from shared_accounts.models import SharedAccount


class SharedAccountBalanceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = SharedAccount
        fields = ["id", "username", "added_at"]


class BalanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.username")
    shared_accounts = SharedAccountBalanceSerializer(
        many=True,
        required=False,
        read_only=True
        )

    class Meta:
        model = Balance
        fields = ["id", "name",  "created_at", "total_incomes",
                  "total_expenses", "total_fixed_expenses", "account_type",
                  "balance", "owner", "shared_accounts"]
