# Generated by Django 4.0.4 on 2022-05-11 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(max_length=40, verbose_name='Fecha')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('description', models.CharField(max_length=30, verbose_name='Descripcion')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.service', verbose_name='Servicio')),
            ],
            options={
                'verbose_name_plural': 'Blog',
                'db_table': 'blog',
                'ordering': ('id',),
            },
        ),
    ]