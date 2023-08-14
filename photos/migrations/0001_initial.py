# Generated by Django 4.0.10 on 2023-08-09 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photographers', '0002_alter_photographer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'рамка',
                'verbose_name_plural': 'рамки',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateField(verbose_name='')),
                ('price', models.FloatField(verbose_name='цена')),
                ('category', models.ManyToManyField(related_name='photos', to='photos.category')),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photographers.photographer')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотки',
            },
        ),
    ]
