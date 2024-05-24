from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):
    guest = models.ForeignKey(
        User, verbose_name='Гость', on_delete=models.CASCADE)
    text = models.TextField('Текст отзыва', max_length=250)
    created_at = models.DateField(
        'Дата создания', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв #{self.id} {self.guest.last_name}'
