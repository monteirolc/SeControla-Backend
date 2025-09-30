from rest_framework import serializers
from .models import FixedIncome, FixedIncomeInstance


class FixedIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedIncome
        fields = '__all__'


class FixedIncomeInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedIncomeInstance
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=False)

        if not valid:
            if raise_exception:
                raise serializers.ValidationError(self.errors)

        return valid
