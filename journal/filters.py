from django_filters import rest_framework as filters

from journal.models import ToiletRecord, FoodRecord, WalkRecord, SleepRecord, GymnasticsRecord, \
    OtherEventRecord, SummaryRecord


class ToiletFilter(filters.FilterSet):
    """Фильтр записей журнала туалета"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = ToiletRecord
        fields = ['category', 'dt']


class FoodFilter(filters.FilterSet):
    """Фильтр записей журнала питания"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = FoodRecord
        fields = ['category', 'dt']


class WalkFilter(filters.FilterSet):
    """Фильтр записей журнала прогулок"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = WalkRecord
        fields = ['dt']


class SleepFilter(filters.FilterSet):
    """Фильтр записей журнала сна"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = SleepRecord
        fields = ['dt']


class GymnasticsFilter(filters.FilterSet):
    """Фильтр записей журнала гимнастики"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = GymnasticsRecord
        fields = ['dt']


class OtherEventFilter(filters.FilterSet):
    """Фильтр записей журнала других событий"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = OtherEventRecord
        fields = ['dt']


class SummaryFilter(filters.FilterSet):
    """Фильтр записей сводного журнала"""
    dt = filters.DateFromToRangeFilter()

    class Meta:
        model = SummaryRecord
        fields = ['dt']
