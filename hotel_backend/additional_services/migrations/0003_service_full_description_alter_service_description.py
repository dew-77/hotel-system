# Generated by Django 4.2.11 on 2024-04-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_services', '0002_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='full_description',
            field=models.TextField(blank=True, null=True, verbose_name='Расширенное описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='Описание услуги'),
        ),
    ]
