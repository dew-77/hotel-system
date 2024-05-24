from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden

from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from rooms.models import Layout, Room
from additional_services.models import Service
from .models import Booking


@login_required
# НАПИШИ КАСТОМНЫЕ ПЕРМИШНЫ is_author_permission
def booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    check_out_date = booking.check_out_date
    check_in_date = booking.check_in_date

    check_out_date_formatted = check_out_date.strftime('%Y%m%d')
    check_in_date_formatted = check_in_date.strftime('%Y%m%d')
    check_out_time_formatted = check_out_date.strftime('%H%M%S')
    check_in_time_formatted = check_in_date.strftime('%H%M%S')

    event_details = f"""
    <div>
        <b>Номер:</b> №{booking.room.number}<br>
        <b>Тип номера:</b> {booking.room.layout_type.name}<br>
        <b>Адрес:</b> ул. Примерная, д. 123, этаж {booking.room.floor},
        комната {booking}
    </div>
    """
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        if request.user == booking.guest:
            booking.is_confirmed = True
            booking.save()
            return render(request, 'bookings/booking_confirmed.html', {
                'booking': booking,
                'check_out_date': check_out_date,
                'check_in_date': check_in_date,
                'check_out_date_formatted': check_out_date_formatted,
                'check_in_date_formatted': check_in_date_formatted,
                'check_out_time_formatted': check_out_time_formatted,
                'check_in_time_formatted': check_in_time_formatted,
                'event_details': event_details
            })
        else:
            return HttpResponseForbidden("Доступ запрещен")
    else:
        return HttpResponseForbidden("Метод не разрешен")


@login_required
def booking_cancel(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        if request.user == booking.guest:
            booking.delete()
            return render(request, 'bookings/booking_cancelled.html')
        else:
            return HttpResponseForbidden("Доступ запрещен")
    else:
        return HttpResponseForbidden("Метод не разрешен")


# Check author
@login_required
def booking_pay(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    total_price = booking.bill

    for additional_service in booking.additional_services.all():
        total_price += additional_service.price
    booking.total_price = total_price
    booking.total_price_part = total_price // 2
    if request.user != booking.guest:
        return redirect('homepage:home')
    return render(request, 'bookings/pay.html', {'booking': booking})


@login_required
def booking_precancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest:
        return redirect('homepage:home')
    return render(request, 'bookings/cancel.html', {'booking': booking})


def book_layout(request, layout_slug):
    layout = get_object_or_404(Layout, slug=layout_slug)
    layout.capacity_person_list = [
        i for i in range(1, layout.capacity_person+1)
    ]
    return render(request, 'bookings/book_layout.html', {'layout': layout})


@login_required
def booking_presuccess(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest or booking.is_confirmed:
        return redirect('homepage:home')
    services = Service.objects.all()

    additional_service_ids = list(booking.additional_services.values_list('id', flat=True))

    return render(
        request, 'bookings/presuccess.html', {
            'booking': booking,
            'additional_service_ids': additional_service_ids,
            'services': services,
        })


@login_required
def check_availability(request):
    if request.method == 'POST' and request.headers.get(
            'x-requested-with') == 'XMLHttpRequest':
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')

        if validate_pair_date(check_in_date, check_out_date):
            layout_slug = request.POST.get('layout_slug')
            layout = get_object_or_404(Layout, slug=layout_slug)

            available_rooms = Room.objects.filter(layout_type=layout)
            bookings = Booking.objects.filter(
                check_in_date__lte=check_out_date,
                check_out_date__gte=check_in_date
            )

            check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
            for booking in bookings:
                available_rooms = available_rooms.exclude(id=booking.room.id)

            if available_rooms.exists():
                num_days = (check_out_date - check_in_date).days

                total_cost = layout.cost_per_day * num_days

                return JsonResponse(
                    {
                        'available': True,
                        'num_days': num_days,
                        'total_cost': total_cost
                    }
                )
            else:
                return JsonResponse({'available': False})
    return JsonResponse({}, status=400)


@login_required
def confirm_booking(request, layout_slug):
    if request.method == 'POST':
        layout = get_object_or_404(Layout, slug=layout_slug)

        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        guests_amount = request.POST.get('capacity')

        if int(guests_amount) > layout.capacity_person:
            error_message = 'Ошибка ввода числа гостей!'
            return render(
                request,
                'bookings/error.html', {'error_message': error_message}
            )

        check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()

        available_rooms = Room.objects.filter(layout_type=layout)

        bookings = Booking.objects.filter(
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date,
        )

        for booking in bookings:
            available_rooms = available_rooms.exclude(id=booking.room.id)

        if available_rooms.exists():
            user = request.user
            num_days = (check_out_date - check_in_date).days
            total_cost = layout.cost_per_day * num_days

            booking = Booking.objects.create(
                room=available_rooms.first(),
                guest=user,
                guests_amount=guests_amount,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                bill=total_cost
            )
            return redirect('bookings:presuccess', booking_id=booking.id)
        else:
            error_message = 'Нет доступных комнат для выбранных дат'
            return render(
                request,
                'bookings/error.html', {'error_message': error_message}
            )
    else:
        return render(
            request,
            'bookings/error.html',
            {'error_message': 'Метод не разрешен'}, status=405
        )


def validate_date(date: str):
    date = date.split('-')
    for element in date:
        if element == '':
            return False
    return True


def validate_pair_date(check_in_date: str, check_out_date: str):
    print(f'{check_out_date} - {check_in_date}')
    if not validate_date(check_out_date) or not validate_date(check_in_date):
        print(f'{check_out_date} - {check_in_date}')
        print('Ошибка в формате даты.')
        return False
    check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
    check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()

    if check_in_date <= timezone.now().date() or \
            check_out_date <= timezone.now().date() or \
            check_in_date >= check_out_date:
        print('Дата не соответствует требованиям.')
        return False
    return True
