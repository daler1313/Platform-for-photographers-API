# Generated by Django 4.0.10 on 2023-08-09 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтингы'},
        ),
    ]