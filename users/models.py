from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Почта',unique=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name='Аватарка')
    phone = PhoneField(max_length=50, verbose_name='Телефон', blank=True, null=True)
    town = models.CharField(max_length=150, verbose_name='Город', blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.email}'

