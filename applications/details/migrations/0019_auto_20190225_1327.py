# Generated by Django 2.1.4 on 2019-02-25 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0018_contrato_idcliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrato',
            old_name='IdCliente',
            new_name='Cliente',
        ),
        migrations.AddField(
            model_name='contrato',
            name='Cajones',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='details.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Impuesto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='details.Impuestos'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Nivel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='details.Edificio'),
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='Cajon',
            field=models.IntegerField(blank=True, default=None, verbose_name='Cajón Número'),
        ),
    ]
