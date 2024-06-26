# Generated by Django 4.2.11 on 2024-04-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_remove_room_amenities_layout_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='accessible_for_disabled',
            field=models.BooleanField(default=1, verbose_name='Доступность для инвалидов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='layout',
            name='number_of_beds',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество кроватей, шт.'),
            preserve_default=False,
        ),
    ]
