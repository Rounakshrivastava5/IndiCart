# Generated by Django 3.0.8 on 2020-07-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
    ]
