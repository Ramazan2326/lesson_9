# Generated by Django 5.0.4 on 2024-05-08 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_alter_actor_first_name_alter_actor_has_oscar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cinema.actor', verbose_name='Актер'),
        ),
    ]
