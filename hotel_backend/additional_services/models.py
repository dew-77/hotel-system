from django.db import models


class Service(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание услуги')
    price = models.PositiveIntegerField('Стоимость')
    image = models.ImageField(
        'Изображение', upload_to='service_photos/')

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'дополнительные услуги'

    def __str__(self):
        return self.name
