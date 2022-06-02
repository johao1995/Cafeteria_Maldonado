# Generated by Django 4.0.4 on 2022-05-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('message', models.CharField(max_length=40, verbose_name='Mensaje')),
            ],
            options={
                'verbose_name_plural': 'Contacto',
                'db_table': 'contact',
                'ordering': ('id',),
            },
        ),
    ]
