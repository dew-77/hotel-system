# Generated by Django 4.2.11 on 2024-04-12 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_layout_remove_room_layout_type_alter_room_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layout',
            options={'verbose_name': 'Планировка', 'verbose_name_plural': 'планировки'},
        ),
        migrations.AlterField(
            model_name='layout',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='layout',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг'),
        ),
        migrations.CreateModel(
            name='LayoutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='layout_photos/', verbose_name='Изображение планировки')),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.layout')),
            ],
        ),
    ]