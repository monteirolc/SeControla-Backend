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

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=False)

        if not valid:
            if raise_exception:
                raise serializers.ValidationError(self.errors)

        return valid
