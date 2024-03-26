from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = '__all__'


class CustomTokenObtainSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom fields
        token['username'] = user.username
        token['email'] = user.email

        return token
