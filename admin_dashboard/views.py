from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from admin_dashboard import mixins
from journal import models
from bjb_toolkit import analytics


class BaseDashboardView(LoginRequiredMixin, generic.ListView):
    """Абстрактный класс для отображения раздела журнала"""
    model = None
    template_name = 'admin_dashboard/index.html'
    context_object_name = 'records'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return super().get_queryset().available(team=user.team).order_by('-dt')


class SummaryDashboardView(BaseDashboardView):
    """Раздел Весь журнал - главная страница админ панели"""
    model = models.SummaryRecord
    template_name = 'admin_dashboard/index.html'
    paginate_by = 15


class ToiletDashboardView(mixins.AnalyticsMixin, BaseDashboardView):
    """Раздел Туалет"""
    model = models.ToiletRecord
    template_name = 'admin_dashboard/toilet.html'
    _analytics_func = analytics.get_toilet_analytics


class ToiletCreatePageView(LoginRequiredMixin, mixins.ToiletCRUDMixin, generic.CreateView):
    """Страница добавления записи туалета"""
    template_name = 'admin_dashboard/record_operation/create.html'


class ToiletUpdatePageView(LoginRequiredMixin, mixins.ToiletCRUDMixin, generic.UpdateView):
    """Страница изменения записи туалета"""
    template_name = 'admin_dashboard/record_operation/update.html'


class ToiletDeletePageView(LoginRequiredMixin, mixins.ToiletCRUDMixin, generic.DeleteView):
    """Страница удаления записи туалета"""
    template_name = 'admin_dashboard/record_operation/delete.html'


class FoodDashboardView(mixins.AnalyticsMixin, BaseDashboardView):
    """Раздел Питание"""
    model = models.FoodRecord
    template_name = 'admin_dashboard/food.html'
    _analytics_func = analytics.get_food_analytics


class FoodCreatePageView(LoginRequiredMixin, mixins.FoodCRUDMixin, generic.CreateView):
    """Страница добавления записи питания"""
    template_name = 'admin_dashboard/record_operation/create.html'


class FoodUpdatePageView(LoginRequiredMixin, mixins.FoodCRUDMixin, generic.UpdateView):
    """Страница изменения записи питания"""
    template_name = 'admin_dashboard/record_operation/update.html'


class FoodDeletePageView(LoginRequiredMixin, mixins.FoodCRUDMixin, generic.DeleteView):
    """Страница удаления записи питания"""
    template_name = 'admin_dashboard/record_operation/delete.html'


class SleepDashboardView(mixins.AnalyticsMixin, BaseDashboardView):
    """Раздел Сон"""
    model = models.SleepRecord
    template_name = 'admin_dashboard/sleep.html'
    _analytics_func = analytics.get_sleep_analytics


class SleepCreatePageView(LoginRequiredMixin, mixins.SleepCRUDMixin, generic.CreateView):
    """Страница добавления записи сна"""
    template_name = 'admin_dashboard/record_operation/create.html'


class SleepUpdatePageView(LoginRequiredMixin, mixins.SleepCRUDMixin, generic.UpdateView):
    """Страница изменения записи сна"""
    template_name = 'admin_dashboard/record_operation/update.html'


class SleepDeletePageView(LoginRequiredMixin, mixins.SleepCRUDMixin, generic.DeleteView):
    """Страница удаления записи сна"""
    template_name = 'admin_dashboard/record_operation/delete.html'


class WalkDashboardView(mixins.AnalyticsMixin, BaseDashboardView):
    """Раздел Прогулки"""
    model = models.WalkRecord
    template_name = 'admin_dashboard/walk.html'
    _analytics_func = analytics.get_walk_analytics


class WalkCreatePageView(LoginRequiredMixin, mixins.WalkCRUDMixin, generic.CreateView):
    """Страница добавления записи прогулки"""
    template_name = 'admin_dashboard/record_operation/create.html'


class WalkUpdatePageView(LoginRequiredMixin, mixins.WalkCRUDMixin, generic.UpdateView):
    """Страница изменения записи прогулки"""
    template_name = 'admin_dashboard/record_operation/update.html'


class WalkDeletePageView(LoginRequiredMixin, mixins.WalkCRUDMixin, generic.DeleteView):
    """Страница удаления записи прогулки"""
    template_name = 'admin_dashboard/record_operation/delete.html'


class GymnasticsDashboardView(mixins.AnalyticsMixin, BaseDashboardView):
    """Раздел Гимнастика"""
    model = models.GymnasticsRecord
    template_name = 'admin_dashboard/gymnastics.html'
    _analytics_func = analytics.get_gymnastics_analytics


class GymnasticsCreatePageView(LoginRequiredMixin, mixins.GymnasticsCRUDMixin, generic.CreateView):
    """Страница добавления записи гимнастики"""
    template_name = 'admin_dashboard/record_operation/create.html'


class GymnasticsUpdatePageView(LoginRequiredMixin, mixins.GymnasticsCRUDMixin, generic.UpdateView):
    """Страница изменения записи гимнастики"""
    template_name = 'admin_dashboard/record_operation/update.html'


class GymnasticsDeletePageView(LoginRequiredMixin, mixins.GymnasticsCRUDMixin, generic.DeleteView):
    """Страница удаления записи гимнастики"""
    template_name = 'admin_dashboard/record_operation/delete.html'


class OtherEventDashboardView(BaseDashboardView):
    """Раздел Другие события"""
    model = models.OtherEventRecord
    template_name = 'admin_dashboard/other_event.html'


class OtherEventCreatePageView(LoginRequiredMixin, mixins.OtherEventCRUDMixin, generic.CreateView):
    """Страница добавления записи другого события"""
    template_name = 'admin_dashboard/record_operation/create.html'


class OtherEventUpdatePageView(LoginRequiredMixin, mixins.OtherEventCRUDMixin, generic.UpdateView):
    """Страница изменения записи другого события"""
    template_name = 'admin_dashboard/record_operation/update.html'


class OtherEventDeletePageView(LoginRequiredMixin, mixins.OtherEventCRUDMixin, generic.DeleteView):
    """Страница удаления записи другого события"""
    template_name = 'admin_dashboard/record_operation/delete.html'