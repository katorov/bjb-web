from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_filter = ('is_paid',)
    list_display = ('username', 'full_name', 'team', 'is_paid')
    list_editable = ('team', 'is_paid')

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'Полное имя'

