# Generated by Django 2.1.4 on 2019-02-25 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0014_merge_20190205_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Nivel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='details.Edificio'),
        ),
    ]
