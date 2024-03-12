from rest_framework.routers import DefaultRouter

from .apps import UsersConfig
from .views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router2 = DefaultRouter()
router2.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    ] + router.urls + router2.urls
