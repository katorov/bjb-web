from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from journal.models import SummaryRecord, FoodRecord, WalkRecord, SleepRecord, OtherEventRecord, \
    ToiletRecord, GymnasticsRecord


def update_summary_record(instance, short_event_type):
    summary_record, _ = SummaryRecord.objects.update_or_create(
        event_id=instance.id,
        event_type=short_event_type,
        defaults={
            'dt': instance.dt,
            'created_by': instance.created_by,
            'team': instance.team,
            'name': dict(SummaryRecord.EVENT_TYPE_CHOICES)[short_event_type],
            'description': instance.get_summary_description()
        }
    )


@receiver(post_save, sender=FoodRecord)
def update_food_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о приеме еды в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.FOOD)


@receiver(post_save, sender=WalkRecord)
def update_walk_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о прогулке в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.WALK)


@receiver(post_save, sender=SleepRecord)
def update_sleep_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о сне в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.SLEEP)


@receiver(post_save, sender=OtherEventRecord)
def update_other_event_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о другом событии в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.OTHER_EVENT)


@receiver(post_save, sender=ToiletRecord)
def update_toilet_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о туалете в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.TOILET)


@receiver(post_save, sender=GymnasticsRecord)
def update_gymnastics_summary_record(sender, instance, **kwargs):
    """Создать/изменить запись о гимнастике в общем журнале событий"""
    update_summary_record(instance=instance, short_event_type=SummaryRecord.GYMNASTICS)


@receiver(post_delete, sender=FoodRecord)
def delete_food_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.FOOD).delete()


@receiver(post_delete, sender=WalkRecord)
def delete_walk_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.WALK).delete()


@receiver(post_delete, sender=SleepRecord)
def delete_sleep_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.SLEEP).delete()


@receiver(post_delete, sender=OtherEventRecord)
def delete_other_event_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.OTHER_EVENT).delete()


@receiver(post_delete, sender=ToiletRecord)
def delete_toilet_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.TOILET).delete()


@receiver(post_delete, sender=GymnasticsRecord)
def delete_gymnastics_summary_record(sender, instance, **kwargs):
    """Удалить запись о приеме еды в общем журнале событий"""
    SummaryRecord.objects.filter(event_id=instance.id,
                                 event_type=SummaryRecord.GYMNASTICS).delete()
