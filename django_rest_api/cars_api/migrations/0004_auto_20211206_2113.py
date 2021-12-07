# Generated by Django 3.2.9 on 2021-12-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_api', '0003_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default='number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='top_speed',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]