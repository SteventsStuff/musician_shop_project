# Generated by Django 2.2 on 2019-04-20 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190420_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='prod_accessories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Accessories', verbose_name='Accessories'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_analog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Analog', verbose_name='Analog'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Comments', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_manufacturer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Manufacturer', verbose_name='Manufacturer'),
        ),
    ]
