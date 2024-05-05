from rest_framework import serializers
from .models import User, Balance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['user', 'amount']