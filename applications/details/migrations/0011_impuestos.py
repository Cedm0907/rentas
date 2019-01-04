# Generated by Django 2.1.4 on 2019-01-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0010_remove_nivel_plano'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default=None, max_length=80, verbose_name='Nombre del impuesto')),
                ('Porcentaje', models.IntegerField(blank=True, verbose_name='Cuota (%)')),
            ],
        ),
    ]