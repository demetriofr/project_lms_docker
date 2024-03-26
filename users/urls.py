from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .apps import UsersConfig
from .views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router2 = DefaultRouter()
router2.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls + router2.urls
