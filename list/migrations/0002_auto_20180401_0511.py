# Generated by Django 2.0.3 on 2018-04-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]
