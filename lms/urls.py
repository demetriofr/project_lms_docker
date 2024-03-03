from rest_framework.routers import DefaultRouter

from .apps import LmsConfig
from .views import CourseViewSet

app_name = LmsConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
