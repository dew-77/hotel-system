# Generated by Django 4.2.11 on 2024-04-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание планировки'),
            preserve_default=False,
        ),
    ]
