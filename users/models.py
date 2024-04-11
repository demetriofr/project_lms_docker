from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'участник'
    MODERATOR = 'moderator', 'модератор'


PAYMENT_METHODS = [
    ('C', 'Наличные'),
    ('T', 'Перевод на счет'),
]


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='электронная почта')

    phone = models.CharField(max_length=15, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=160, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    data_paid = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')

    course = models.ForeignKey('lms.Course', on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey('lms.Lesson', on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)

    sum_paid = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS, verbose_name='метод оплаты', default='C')

    def __str__(self):
        return f'''{self.user} оплатил(-а) курс или урок {self.course.name if self.course else self.lesson.name} 
        на сумму {self.sum_paid}'''

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платёжи'
