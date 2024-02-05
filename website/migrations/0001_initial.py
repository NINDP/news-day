# Generated by Django 5.0.1 on 2024-01-22 12:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('published_at', models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 14, 57, 22857), verbose_name='Опубликовать в')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.categories', verbose_name='Категория')),
            ],
        ),
    ]