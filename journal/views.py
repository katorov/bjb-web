from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from journal.filters import ToiletFilter, FoodFilter, WalkFilter, SleepFilter, GymnasticsFilter, \
    OtherEventFilter, SummaryFilter
from journal.mixins import AvailableRecordsMixin
from journal.models import ToiletRecord, FoodRecord, WalkRecord, SleepRecord, GymnasticsRecord, \
    OtherEventRecord, SummaryRecord
from journal.serializers import ToiletSerializer, FoodSerializer, WalkSerializer, SleepSerializer, \
    GymnasticsSerializer, OtherEventSerializer, SummarySerializer


class ToiletRetrieveUpdateDestroyView(AvailableRecordsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ToiletRecord.objects.all()
    serializer_class = ToiletSerializer


class ToiletListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    serializer_class = ToiletSerializer
    filterset_class = ToiletFilter
    queryset = ToiletRecord.objects.all()


class FoodRetrieveUpdateDestroyView(AvailableRecordsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRecord.objects.all()
    serializer_class = FoodSerializer


class FoodListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    queryset = FoodRecord.objects.all()
    serializer_class = FoodSerializer
    filterset_class = FoodFilter


class WalkRetrieveUpdateDestroyView(AvailableRecordsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = WalkRecord.objects.all()
    serializer_class = WalkSerializer


class WalkListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    queryset = WalkRecord.objects.all()
    serializer_class = WalkSerializer
    filterset_class = WalkFilter


class SleepRetrieveUpdateDestroyView(AvailableRecordsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SleepRecord.objects.all()
    serializer_class = SleepSerializer


class SleepListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    queryset = SleepRecord.objects.all()
    serializer_class = SleepSerializer
    filterset_class = SleepFilter


class GymnasticsRetrieveUpdateDestroyView(AvailableRecordsMixin,
                                          generics.RetrieveUpdateDestroyAPIView):
    queryset = GymnasticsRecord.objects.all()
    serializer_class = GymnasticsSerializer


class GymnasticsListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    queryset = GymnasticsRecord.objects.all()
    serializer_class = GymnasticsSerializer
    filterset_class = GymnasticsFilter


class OtherEventRetrieveUpdateDestroyView(AvailableRecordsMixin,
                                          generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherEventRecord.objects.all()
    serializer_class = OtherEventSerializer


class OtherEventListCreateView(AvailableRecordsMixin, generics.ListCreateAPIView):
    queryset = OtherEventRecord.objects.all()
    serializer_class = OtherEventSerializer
    filterset_class = OtherEventFilter


class SummaryRetrieveView(AvailableRecordsMixin, generics.RetrieveAPIView):
    queryset = SummaryRecord.objects.all()
    serializer_class = SummarySerializer


class SummaryListView(AvailableRecordsMixin, generics.ListAPIView):
    queryset = SummaryRecord.objects.all()
    serializer_class = SummarySerializer
    filterset_class = SummaryFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['dt']
