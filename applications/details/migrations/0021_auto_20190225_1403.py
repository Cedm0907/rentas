# Generated by Django 2.1.4 on 2019-02-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0020_auto_20190225_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='Nivel',
            field=models.PositiveIntegerField(blank=True, verbose_name='Nivel'),
        ),
    ]
