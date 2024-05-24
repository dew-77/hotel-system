from django.db import models
from django.contrib.auth import get_user_model

from datetime import date

from rooms.models import Room
from additional_services.models import Service

User = get_user_model()


class Booking(models.Model):
    """Модель бронирования номера."""
    room = models.ForeignKey(
        Room, verbose_name='Номер', on_delete=models.CASCADE)
    guest = models.ForeignKey(
        User, verbose_name='Гость', on_delete=models.CASCADE)
    guests_amount = models.PositiveIntegerField(
        'Число гостей, которые будут проживать в номере')
    created_at = models.DateField(
        'Дата создания', auto_now=False, auto_now_add=True)
    check_in_date = models.DateField('Дата въезда')
    check_out_date = models.DateField('Дата выезда')
    bill = models.PositiveIntegerField('Стоимость бронирования')
    additional_services = models.ManyToManyField(
        Service, blank=True,
        verbose_name='Дополнительные услуги')
    is_confirmed = models.BooleanField('Подтверждена', default=False)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'бронирования'

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.check_in_date < date.today():
            raise ValidationError('Дата въезда меньше текущего времени.')
        if self.check_in_date >= self.check_out_date:
            raise ValidationError('Дата выезда должна быть позже даты заезда!')
        if self.room.layout_type.capacity_person < self.guests_amount:
            raise ValidationError('Кол-во гостей превышает вместимость!')

    def __str__(self):
        return f'Бронь {self.id} от {self.created_at}'
