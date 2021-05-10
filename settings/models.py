from django.db import models


class TimestampModel(models.Model):
    """Абстрактная модель с полями даты создания и даты изменения"""
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, db_index=True)

    class Meta:
        abstract = True
