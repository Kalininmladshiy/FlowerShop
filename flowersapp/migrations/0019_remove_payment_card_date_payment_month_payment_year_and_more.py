# Generated by Django 4.1.5 on 2023-01-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowersapp', '0018_alter_shop_store_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='card_date',
        ),
        migrations.AddField(
            model_name='payment',
            name='month',
            field=models.CharField(db_index=True, max_length=2, null=True, verbose_name='Месяц конца работы карты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='year',
            field=models.CharField(db_index=True, max_length=2, null=True, verbose_name='Год конца работы карты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Адрес доставки'),
        ),
    ]
