# Generated by Django 2.2.12 on 2021-07-11 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210710_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
