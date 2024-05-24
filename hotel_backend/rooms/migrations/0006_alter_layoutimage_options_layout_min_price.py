# Generated by Django 4.2.11 on 2024-04-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_layout_options_alter_layout_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layoutimage',
            options={'verbose_name': 'Изображение планировки', 'verbose_name_plural': 'изображения планировок'},
        ),
        migrations.AddField(
            model_name='layout',
            name='min_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Минимальная цена'),
        ),
    ]