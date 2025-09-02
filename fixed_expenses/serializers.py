from rest_framework import serializers
from .models import FixedExpense, FixedExpenseInstance


class FixedExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedExpense
        fields = '__all__'


class FixedExpenseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedExpenseInstance
        fields = '__all__'
