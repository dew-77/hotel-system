# Generated by Django 5.0.4 on 2024-04-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='facilities',
            new_name='amenities',
        ),
        migrations.AlterField(
            model_name='amenity',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]