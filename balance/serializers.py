from rest_framework import serializers
from .models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    total_expenses = serializers.SerializerMethodField()
    total_incomes = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Balance
        fields = '__all__'

    def get_total_expenses(self, obj):
        return obj.total_expenses()

    def get_total_incomes(self, obj):
        return obj.total_incomes()

    def get_balance(self, obj):
        return obj.balance()
