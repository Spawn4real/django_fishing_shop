from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=64, verbose_name='Город', blank=True)
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона', blank=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, verbose_name='Аватар')