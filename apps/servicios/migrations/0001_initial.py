# Generated by Django 4.0.4 on 2022-05-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=40, verbose_name='SubTitulo')),
                ('description', models.CharField(max_length=40, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='media/servicios/img', verbose_name='Imagen')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
                'db_table': 'service',
                'ordering': ('id',),
            },
        ),
    ]
