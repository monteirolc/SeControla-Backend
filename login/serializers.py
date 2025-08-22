from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'last_name', 'age', 'cpf', 'email', 'phone',
                  'login', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(login=data.get('login'),
                            password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid login credentials")
        return data
