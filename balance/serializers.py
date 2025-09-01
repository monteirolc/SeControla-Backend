from rest_framework import serializers
from .models import Balance
from django.contrib.auth import get_user_model

User = get_user_model()


class BalanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.username")
    # shared_accounts = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field="username",
    #     queryset=User.objects.all(),
    #     required=False
    # )

    class Meta:
        model = Balance
        fields = ["id", "name",  "created_at", "total_incomes",
                  "total_expenses", "account_type", "owner"]
# , "shared_accounts"]
