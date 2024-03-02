from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='электронная почта')

    phone = models.CharField(max_length=15, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=160, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
