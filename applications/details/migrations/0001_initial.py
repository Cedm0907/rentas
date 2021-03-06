# Generated by Django 2.1.5 on 2019-02-02 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default=None, max_length=80, verbose_name='Razón Social | Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo electrónico')),
                ('direccion', models.CharField(default=None, max_length=300, verbose_name='Domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Folio', models.CharField(default=None, max_length=80, verbose_name='Número de contrato')),
                ('Metros_contratados', models.IntegerField(blank=True, verbose_name='Metros arrendados')),
                ('Precio_metro', models.DecimalField(blank=True, decimal_places=2, max_digits=6, max_length=80, verbose_name='Precio por metro cuadrado')),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=80, verbose_name='Nombre')),
                ('Nivel', models.CharField(blank=True, max_length=80, verbose_name='Nivel')),
                ('Metros', models.FloatField(blank=True, max_length=80, verbose_name='Metros')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UsoCajon', models.CharField(choices=[('PC', 'Contrato'), ('PS', 'Pensión'), ('HR', 'Renta por Hora')], default='PC', max_length=80, verbose_name='Uso de cajón')),
            ],
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default=None, max_length=80, verbose_name='Nombre del impuesto')),
                ('Porcentaje', models.IntegerField(blank=True, verbose_name='Cuota (%)')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Metros', models.DecimalField(blank=True, decimal_places=2, max_digits=6, max_length=80, verbose_name='Metros')),
                ('Sanitarios', models.IntegerField(blank=True, verbose_name='Número de Baños')),
                ('Nivel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='details.Edificio')),
            ],
        ),
    ]
