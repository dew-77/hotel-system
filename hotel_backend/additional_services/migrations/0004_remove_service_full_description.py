# Generated by Django 4.2.11 on 2024-04-22 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additional_services', '0003_service_full_description_alter_service_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='full_description',
        ),
    ]
