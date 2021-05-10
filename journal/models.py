from abc import abstractmethod

from django.db import models
from django.urls import reverse, reverse_lazy

from settings.models import TimestampModel
from users.models import User


class AbstractRecordQuerySet(models.QuerySet):
    """Queryset с возможностью отобразить только доступные записи своей команды"""
    def available(self, team):
        """Получить только записи указанной команды"""
        return self.filter(team=team)


class AbstractRecord(TimestampModel):
    """Абстрактная модель записи журнала"""
    dt = models.DateTimeField('Дата/время', db_index=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Создал',
        related_name='created_%(class)s'
    )
    team = models.BigIntegerField('Команда')

    objects = AbstractRecordQuerySet.as_manager()

    @abstractmethod
    def get_summary_description(self):
        pass

    class Meta:
        abstract = True


class SummaryRecord(AbstractRecord):
    """Запись из 'сводного' журнала, который хранит записи всех журналов в едином стиле"""
    FOOD, WALK, GYMNASTICS, OTHER_EVENT, SLEEP, TOILET = 'еда', 'прг', 'гим', 'др', 'сон', 'тлт'
    EVENT_TYPE_CHOICES = (
        (FOOD, 'Питание'),
        (WALK, 'Прогулка'),
        (GYMNASTICS, 'Гимнастика'),
        (OTHER_EVENT, 'Другое событие'),
        (SLEEP, 'Сон'),
        (TOILET, 'Туалет'),
    )

    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    event_id = models.BigIntegerField('ID события')
    event_type = models.CharField('Тип события', choices=EVENT_TYPE_CHOICES, max_length=3)

    class Meta:
        verbose_name = 'Запись журнала'
        verbose_name_plural = 'Записи журнала'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.name}'

    def get_summary_description(self):
        return self.description

    def get_update_link(self):
        event_id = self.event_id
        event_update_links = {
            self.FOOD: reverse('upd_toilet', args=[event_id]),
            self.WALK: reverse('upd_toilet', args=[event_id]),
            self.GYMNASTICS: reverse('upd_toilet', args=[event_id]),
            self.OTHER_EVENT: reverse('upd_toilet', args=[event_id]),
            self.SLEEP: reverse('upd_toilet', args=[event_id]),
            self.TOILET: reverse_lazy('upd_toilet', args=[event_id]),
        }
        return event_update_links[self.event_type]

    def get_delete_link(self):
        event_id = self.event_id
        event_update_links = {
            self.FOOD: reverse('del_toilet', args=[event_id]),
            self.WALK: reverse('del_toilet', args=[event_id]),
            self.GYMNASTICS: reverse('del_toilet', args=[event_id]),
            self.OTHER_EVENT: reverse('del_toilet', args=[event_id]),
            self.SLEEP: reverse('del_toilet', args=[event_id]),
            self.TOILET: reverse_lazy('del_toilet', args=[event_id]),
        }
        return event_update_links[self.event_type]


class FoodRecord(AbstractRecord):
    """Запись из журнала приемов пищи"""
    MILK, WATER, NUTRITION = 'м', 'в', 'п'
    FOOD_TYPE_CHOICES = (
        (MILK, 'Молоко'),
        (WATER, 'Вода'),
        (NUTRITION, 'Пища'),
    )

    category = models.CharField(
        'Категория', max_length=3, choices=FOOD_TYPE_CHOICES, default=NUTRITION
    )
    name = models.CharField('Название еды', max_length=100, blank=True)
    quantity = models.PositiveIntegerField('Количество')

    class Meta:
        verbose_name = 'Прием еды'
        verbose_name_plural = 'Приемы еды'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.category} {self.name} - {self.quantity} гр'

    def get_summary_description(self):
        if self.category != self.NUTRITION:
            name = self.get_category_display()
        else:
            name = f'{self.get_category_display()}, {self.name}'
        return f'{name}: {self.quantity} гр'


class GymnasticsRecord(AbstractRecord):
    """Запись из журнала гимнастики"""
    duration = models.PositiveIntegerField('Длительность, мин')

    class Meta:
        verbose_name = 'Гимнастика'
        verbose_name_plural = 'Гимнастика'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.duration} мин'

    def get_summary_description(self):
        return f'{self.duration} мин'


class SleepRecord(AbstractRecord):
    """Запись из журнала сна"""
    duration = models.PositiveIntegerField('Длительность, мин')

    class Meta:
        verbose_name = 'Сон'
        verbose_name_plural = 'Сон'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.duration} мин'

    def get_summary_description(self):
        return f'{self.duration} мин'


class OtherEventRecord(AbstractRecord):
    """Запись из журнала других событий"""
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Другое событие'
        verbose_name_plural = 'Другие события'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.name}'

    def get_summary_description(self):
        return self.name + '\n' + self.description


class ToiletRecord(AbstractRecord):
    """Запись из журнала туалета"""
    TOILET_CATEGORY_CHOICES = (
        (1, 'Мало'),
        (2, 'Как обычно'),
        (3, 'Много'),
        (4, 'Реально шок'),
    )
    category = models.PositiveSmallIntegerField("Категория", choices=TOILET_CATEGORY_CHOICES)

    class Meta:
        verbose_name = 'Туалет'
        verbose_name_plural = 'Туалет'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.get_category_display()}'

    def get_summary_description(self):
        return f'{self.category}: {self.get_category_display()}'


class WalkRecord(AbstractRecord):
    """Запись из журнала прогулок"""
    duration = models.PositiveIntegerField('Длительность, мин')

    class Meta:
        verbose_name = 'Прогулка'
        verbose_name_plural = 'Прогулки'
        ordering = ['dt']

    def __str__(self):
        return f'{self.dt}: {self.duration} мин'

    def get_summary_description(self):
        return f'{self.duration} мин'
