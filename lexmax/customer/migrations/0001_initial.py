# Generated by Django 4.0.4 on 2022-05-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('address', models.CharField(max_length=50, verbose_name='Dirrecion')),
                ('reference_address', models.CharField(max_length=50, verbose_name='Referencia de la dirección')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created_at'],
            },
        ),
    ]
