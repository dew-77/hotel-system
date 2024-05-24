from django.views.generic import ListView

from reviews.models import Review
from rooms.models import Layout


HOME_MAX_LAYOUTS = 6
HOME_MAX_REVIEWS = 3


class MainPageView(ListView):
    model = Layout
    context_object_name = 'layouts'
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        layouts = Layout.objects.all()[:HOME_MAX_LAYOUTS]
        reviews = Review.objects.all()[:HOME_MAX_REVIEWS]
        context['layouts'] = layouts
        context['reviews'] = reviews

        return context
