# Generated by Django 2.1.4 on 2018-12-31 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20181231_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edificio',
            name='Nivel',
        ),
    ]
