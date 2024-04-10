from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .apps import UsersConfig
from .views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, PaymentViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
