from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from bookings.models import Booking
from .forms import RegistrationForm
from .models import CustomUser

User = get_user_model()


class MyBookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "users/my_bookings.html"
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        bookings = Booking.objects.filter(guest=user)
        total_services = bookings.aggregate(total_services=Sum('additional_services'))

        context['user'] = user
        context['bookings'] = bookings
        context['total_services'] = total_services.get('total_services', 0)
        return context


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_redirect_url(self):
        redirect_to = super().get_redirect_url()
        if self.request.user.is_authenticated:
            return reverse_lazy('homepage:home')
        return redirect_to


class CustomRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage:home')

    def form_valid(self, form):
        try:
            user = CustomUser.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                patronymic=form.cleaned_data['patronymic'],
                phone_number=form.cleaned_data['phone_number']
            )
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())
