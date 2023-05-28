from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):

    full_name = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)

    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + [
        'full_name',
        'location',
    ]

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'