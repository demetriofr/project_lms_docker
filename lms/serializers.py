from rest_framework import serializers

from .models import Course, Lesson
from .validators import ExceptYouTubeValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [ExceptYouTubeValidator('link_video')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'


    @staticmethod
    def get_count_lessons(instance):
        """
        Return the count of lessons for the given instance.
        """
        return instance.lesson_set.count()
