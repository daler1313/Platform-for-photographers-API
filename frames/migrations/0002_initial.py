# Generated by Django 4.0.10 on 2023-08-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photographers', '0001_initial'),
        ('frames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='photographers.photographer'),
        ),
    ]
