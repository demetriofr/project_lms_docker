from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Course, Lesson, Subscribe
from .serializers import CourseSerializer, LessonSerializer, SubscribeSerializer
from .permissions import IsModerator, IsOwner
from .paginators import LmsPagination


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LmsPagination

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'update']:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action in ['destroy']:
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LmsPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribeCreateAPIView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user  # получаем текущего пользователя из self.request
        course_id = self.request.data.get('id')  # получаем id курса из self.request.data
        # получаем объект курса из базы с помощью get_object_or_404
        course_item = get_object_or_404(Course, id=course_id)
        # получаем объекты подписок по текущему пользователю и курса
        subs_item = Subscribe.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            # Если подписка у пользователя на этот курс есть - удаляем ее
            subs_item.delete()
            message = 'подписка удалена'
        else:
            # Если подписки у пользователя на этот курс нет - создаем ее
            Subscribe.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response(f"message: {message}")


