# Generated by Django 2.1.5 on 2019-02-27 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0034_auto_20190227_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impuesto',
            old_name='Porcentaje',
            new_name='PorcentajeTHIS',
        ),
    ]
