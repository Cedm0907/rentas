# Generated by Django 2.1.5 on 2019-03-01 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0041_auto_20190227_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='Fecha_i',
            field=models.DateField(default=datetime.datetime(2019, 3, 1, 17, 10, 26, 472356, tzinfo=utc)),
            preserve_default=False,
        ),
    ]