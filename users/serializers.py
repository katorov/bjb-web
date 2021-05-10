from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class CurrentUserDefault:
    """Текущий пользователь из запроса request"""
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class CurrentUserTeamDefault:
    """Текущая команда пользователя из запроса request"""
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.team


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',
                  'is_paid', 'team', 'invite_link', 'timezone')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'is_paid', 'team', 'invite_link', 'timezone')

