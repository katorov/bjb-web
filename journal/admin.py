from django.contrib import admin

from journal.models import SummaryRecord, FoodRecord, GymnasticsRecord, SleepRecord, OtherEventRecord, \
    WalkRecord, ToiletRecord


@admin.register(SummaryRecord)
class SummaryRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'event_id', 'name', 'dt', 'team')
    list_filter = ('event_type', 'dt')


@admin.register(FoodRecord)
class FoodRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'dt', 'team')
    list_filter = ('category', 'dt')


@admin.register(GymnasticsRecord)
class GymnasticsRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'dt', 'team')
    list_filter = ('dt',)


@admin.register(SleepRecord)
class SleepRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'dt', 'team')
    list_filter = ('dt',)


@admin.register(OtherEventRecord)
class OtherEventRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'dt', 'team')
    list_filter = ('dt',)


@admin.register(WalkRecord)
class WalkRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'dt', 'team')
    list_filter = ('dt',)


@admin.register(ToiletRecord)
class ToiletRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'dt', 'team')
    list_filter = ('category', 'dt',)
