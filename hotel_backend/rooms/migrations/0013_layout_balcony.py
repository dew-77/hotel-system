# Generated by Django 4.2.11 on 2024-04-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_layout_possible_with_children_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='balcony',
            field=models.BooleanField(default=1, verbose_name='Наличие балкона'),
            preserve_default=False,
        ),
    ]
