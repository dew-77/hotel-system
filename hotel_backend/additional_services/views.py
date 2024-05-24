from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from .models import Service
from bookings.models import Booking


def submit_services(request):
    if request.method == 'POST':
        selected_service_unformatted = request.POST.get('selected_service_ids')
        booking_id = request.POST.get('booking_id')
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return JsonResponse(
                {'error': 'Такого бронирования не существует'}, status=404)

        selected_service_ids = selected_service_unformatted.split('_')

        for service_id in selected_service_ids:
            try:
                service = Service.objects.get(id=service_id)
                booking.additional_services.add(service)
            except Service.DoesNotExist:
                pass

        response_data = {'message': 'Услуги успешно добавлены'}
        return JsonResponse(response_data)

    else:
        return JsonResponse(
            {'error': 'Метод запроса должен быть POST'}, status=405)


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
