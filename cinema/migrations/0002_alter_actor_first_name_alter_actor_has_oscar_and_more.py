# Generated by Django 5.0.4 on 2024-05-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='has_oscar',
            field=models.BooleanField(default=False, verbose_name='Лауреат Оскара'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Прозвище'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Описание фильма'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('fantasy', 'Фэнтези'), ('adventures', 'Приключения'), ('action', 'Боевик'), ('drama', 'Драма'), ('thriller', 'Триллер'), ('comedy', 'Комедия')], max_length=20, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='premiere',
            field=models.DateField(verbose_name='Дата премьеры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='Название'),
        ),
    ]
