from asgiref.sync import async_to_sync
from django.urls import reverse_lazy

from admin_dashboard.utils import compute_queryset
from journal import forms
from journal import models


class AnalyticsMixin:
    """Mixin для добавления аналитического графика в контекст"""
    _analytics_func: "Функция, возвращающая график"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = self.get_queryset()
        compute_queryset(records)
        if not records:
            return context

        analytics_func = self.__class__._analytics_func
        fig, _ = analytics_func(records, timezone=self.request.user.timezone)
        if not fig:
            return context

        graph = fig.to_html(full_html=False, default_height=500, include_plotlyjs=False)
        context['analytics'] = graph
        return context


class BaseRecordCRUDMixin:
    """Mixin для автозаполнения полей created_by и team"""

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.team = self.request.user.team
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Записать форму редактирования в контекст"""
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            # В шаблоне удаления записи будет отражена форма
            context['form'] = self.form_class(instance=self.get_object())
        return context


class ToiletCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи туалета"""
    model = models.ToiletRecord
    form_class = forms.ToiletForm
    success_url = reverse_lazy('toilet')
    extra_context = {'title': 'Туалет'}


class FoodCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи питания"""
    model = models.FoodRecord
    form_class = forms.FoodForm
    success_url = reverse_lazy('food')
    extra_context = {'title': 'Питание'}


class SleepCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи сна"""
    model = models.SleepRecord
    form_class = forms.SleepForm
    success_url = reverse_lazy('sleep')
    extra_context = {'title': 'Сон'}


class WalkCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи прогулки"""
    model = models.WalkRecord
    form_class = forms.WalkForm
    success_url = reverse_lazy('walk')
    extra_context = {'title': 'Прогулки'}


class GymnasticsCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи гимнастики"""
    model = models.GymnasticsRecord
    form_class = forms.GymnasticsForm
    success_url = reverse_lazy('gymnastics')
    extra_context = {'title': 'Гимнастика'}


class OtherEventCRUDMixin(BaseRecordCRUDMixin):
    """Mixin с мета-данными для добавления/изменения/удаления записи другого события"""
    model = models.OtherEventRecord
    form_class = forms.OtherEventForm
    success_url = reverse_lazy('other_event')
    extra_context = {'title': 'Другие события'}
