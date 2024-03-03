from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название', unique=True)
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название', unique=True)
    preview = models.ImageField(upload_to='lessons/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ManyToManyField(Course, verbose_name='курс')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
