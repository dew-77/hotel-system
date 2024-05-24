from bookings.models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['text']
    success_url = reverse_lazy('reviews:list')

    def form_valid(self, form):
        form.instance.guest = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_confirmed_booking'] = Booking.objects.filter(
            guest=self.request.user, is_confirmed=True).exists()
        context['has_review'] = Review.objects.filter(
            guest=self.request.user).exists()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    paginate_by = 9
