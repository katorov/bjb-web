class AvailableRecordsMixin:
    """Mixin для отображения только доступных записей журнала"""

    def get_queryset(self):
        team = self.request.user.team
        if not team:
            return self.queryset.none()
        return self.queryset.available(team)
