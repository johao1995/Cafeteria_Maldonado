# Generated by Django 4.0.4 on 2022-06-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='message',
            field=models.TextField(verbose_name='Mensaje'),
        ),
    ]
