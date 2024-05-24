from django.db import models


class Amenity(models.Model):
    """Модель дополнительного удобства."""

    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Удобство'
        verbose_name_plural = 'удобства'

    def __str__(self):
        return self.name


class Layout(models.Model):
    name = models.CharField('Название', max_length=30, unique=True)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание планировки')
    capacity_person = models.PositiveIntegerField('Вместимость, чел')
    number_of_beds = models.PositiveIntegerField('Количество кроватей, шт.')
    accessible_for_disabled = models.BooleanField('Доступность для инвалидов')
    balcony = models.BooleanField('Наличие балкона')
    possible_with_children = models.BooleanField('Можно с детьми')
    possible_with_pets = models.BooleanField('Можно с животными')
    amenities = models.ManyToManyField(
        Amenity, verbose_name='Удобства')
    cost_per_day = models.PositiveIntegerField(
        'Стоимость проживания (р/день)')

    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'планировки'

    def __str__(self):
        return f'Планировка - {self.name}'


class LayoutImage(models.Model):
    layout = models.ForeignKey(
        Layout, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        'Изображение планировки', upload_to='layout_photos/')

    class Meta:
        verbose_name = 'Изображение планировки'
        verbose_name_plural = 'изображения планировок'

    def __str__(self):
        return f'Изображение планировки - {self.layout.name}'


class Room(models.Model):
    """Модель номера гостиницы."""

    number = models.PositiveIntegerField(
        'Номер комнаты/апартаментов', unique=True)
    floor = models.PositiveIntegerField('Этаж')
    layout_type = models.ForeignKey(
        Layout, verbose_name='Тип планировки', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'комнаты'

    def __str__(self):
        return f'Комната №{self.number}'
