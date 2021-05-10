from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь сайта, он же пользователь telegram бота"""
    timezone = models.CharField('Временная зона', max_length=255, default='Europe/Moscow')
    invite_link = models.CharField('Ссылка для приглашения в команду', max_length=255, blank=True)
    is_paid = models.BooleanField('Доступ оплачен', default=False)
    team = models.BigIntegerField('Команда', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

