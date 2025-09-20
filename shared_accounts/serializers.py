from rest_framework import serializers
from .models import SharedAccount


class SharedAccountSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username",
                                          read_only=True)
    balance_name = serializers.CharField(source="balance.name",
                                         read_only=True)

    class Meta:
        model = SharedAccount
        fields = ["id", "user", "user_username", "first_name_shared",
                  "balance_name"]
        read_only_fields = ["created_at"]

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=False)

        if not valid:
            if raise_exception:
                raise serializers.ValidationError(self.errors)

        return valid
