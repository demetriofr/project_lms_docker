from rest_framework.routers import DefaultRouter
from django.urls import path

from .apps import LmsConfig
from .views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView,
                    LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView,
                    SubscribeCreateAPIView)

app_name = LmsConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe-post'),
] + router.urls
