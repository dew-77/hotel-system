# Generated by Django 4.2.11 on 2024-04-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_remove_layout_min_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='capacity_person',
            field=models.PositiveIntegerField(default=1, verbose_name='Вместимость, чел'),
            preserve_default=False,
        ),
    ]