from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from journal.models import ToiletRecord, FoodRecord, WalkRecord, SleepRecord, GymnasticsRecord, \
    OtherEventRecord, SummaryRecord
from users.serializers import CurrentUserDefault, CurrentUserTeamDefault


class BaseJournalRecordSerializer(ModelSerializer):
    """Абстрактный сериализатор для любой записи журнала"""

    def to_representation(self, instance):
        """Выводить username телеграм пользователя вместо id"""
        rep = super().to_representation(instance)
        rep['created_by'] = instance.created_by.username
        return rep

    def validate(self, data):
        """Проверить текущего пользователя на соответствие входным данным"""
        user = self.context['request'].user
        team = getattr(user, 'team', None)

        if not team:
            raise ValidationError('Пользователь не состоит в команде')
        if data['team'] != team:
            raise ValidationError('Вы не состоите в этой команде')
        if data['created_by'] != user:
            raise ValidationError('Вы не можете указать другого пользователя в created_by')

        return data


class ToiletSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала туалета"""

    class Meta:
        model = ToiletRecord
        fields = ['id', 'category', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class FoodSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала еды"""

    class Meta:
        model = FoodRecord
        fields = ['id', 'category', 'name', 'quantity', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class WalkSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала прогулок"""

    class Meta:
        model = WalkRecord
        fields = ['id', 'duration', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class SleepSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала сна"""

    class Meta:
        model = SleepRecord
        fields = ['id', 'duration', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class GymnasticsSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала гимнастики"""

    class Meta:
        model = GymnasticsRecord
        fields = ['id', 'duration', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class OtherEventSerializer(BaseJournalRecordSerializer):
    """Serializer для записи из журнала других событий"""

    class Meta:
        model = OtherEventRecord
        fields = ['id', 'name', 'description', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }


class SummarySerializer(BaseJournalRecordSerializer):
    """Serializer для записи из сводного журнала"""

    class Meta:
        model = SummaryRecord
        fields = ['id', 'name', 'description', 'event_id', 'event_type', 'dt', 'team', 'created_by']
        extra_kwargs = {
            'created_by': {'default': CurrentUserDefault()},
            'team': {'default': CurrentUserTeamDefault()}
        }
