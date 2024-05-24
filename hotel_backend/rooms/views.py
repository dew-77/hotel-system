from django.db.models import Min
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Layout, Room


class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'


class LayoutListView(ListView):
    model = Layout
    context_object_name = 'layouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LayoutDetailView(DetailView):
    model = Layout
    context_object_name = 'layout'

    def get_object(self, queryset=None):
        return get_object_or_404(Layout, slug=self.kwargs['slug'])
