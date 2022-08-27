from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


def default_key_expiration_date():
    return timezone.now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, verbose_name='Город', blank=True)
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона', blank=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", default=18)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, verbose_name='Аватар')

    activation_key = models.CharField(max_length=128, blank=True, verbose_name="ключ активации")
    activation_key_expires = models.DateTimeField(verbose_name="Активация истекает", default=default_key_expiration_date())

    def is_activation_key_expired(self):
        if timezone.now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    NONBINARY = 'X'

    GENDER_CHOICES = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (NONBINARY, 'Небинарный')
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)

    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='гендер', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
