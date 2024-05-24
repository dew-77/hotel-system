from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import CustomUser


class SuperuserFilter(SimpleListFilter):
    title = 'Тип пользователя'
    parameter_name = 'is_superuser'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Суперпользователь'),
            ('no', 'Обычный пользователь'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_superuser=True)
        if self.value() == 'no':
            return queryset.filter(is_superuser=False)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'name_display', 'phone_number', 'is_superuser_display')
    list_filter = (SuperuserFilter,)
    search_fields = ('email', 'phone_number', 'last_name', 'first_name')

    def is_superuser_display(self, obj):
        return 'Да' if obj.is_superuser else 'Нет'

    def name_display(self, obj):
        return f'{obj.last_name} {obj.first_name}'

    is_superuser_display.short_description = 'Суперпользователь'
    name_display.short_description = 'Фамилия Имя'
