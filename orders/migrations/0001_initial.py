# Generated by Django 4.0.10 on 2023-08-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'В ожидании'), ('CONFIRMED', 'Подтвержден'), ('COMPLETED', 'Выполнен'), ('CANCELED', 'Отменен')], default='PENDING', max_length=25, verbose_name='статус заказа')),
                ('created_at', models.DateTimeField(verbose_name='дата и время заказа')),
            ],
            options={
                'verbose_name': 'заказа',
                'verbose_name_plural': 'заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frames.frame')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetails', to='orders.order')),
            ],
            options={
                'verbose_name': 'детали заказа',
                'verbose_name_plural': 'детали заказы',
            },
        ),
    ]
