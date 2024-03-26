from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer, CustomTokenObtainSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_methode']
    ordering_fields = ['data_paid']


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
