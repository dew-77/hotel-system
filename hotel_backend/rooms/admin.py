from django.contrib import admin
from .models import Amenity, Room, Layout, LayoutImage


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'layout_type')
    list_filter = ('layout_type', 'floor')
    search_fields = ('number',)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'layouts_with_amenity')

    def layouts_with_amenity(self, obj):
        return obj.layout_set.count()

    layouts_with_amenity.short_description = 'Количество комнат'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('room_set')
        return queryset


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('amenities',)


@admin.register(LayoutImage)
class LayoutImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'layout', 'image')
    list_filter = ('layout',)
