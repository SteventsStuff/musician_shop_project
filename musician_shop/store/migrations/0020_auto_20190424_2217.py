# Generated by Django 2.2 on 2019-04-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_store_prod_updated_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='prod_rate',
        ),
        migrations.AddField(
            model_name='store',
            name='prod_score_dislikes',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Dislike'),
        ),
        migrations.AddField(
            model_name='store',
            name='prod_score_likes',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Like'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_updated_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Actual price'),
        ),
    ]