# Generated by Django 4.0.10 on 2023-08-09 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользовател', 'verbose_name_plural': 'Пользователы'},
        ),
    ]
