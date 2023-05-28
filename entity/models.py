from django.conf import settings
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Сущность'
        verbose_name_plural = 'Сущности'
