# Generated by Django 2.2 on 2019-04-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_currency_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='cur_EUR',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='currency',
            name='cur_RUB',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='currency',
            name='cur_USD',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=10),
        ),
    ]
