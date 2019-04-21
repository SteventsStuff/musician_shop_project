# Generated by Django 2.2 on 2019-04-20 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_store_prod_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='prod_type',
        ),
        migrations.AlterField(
            model_name='store',
            name='prod_analog',
            field=models.ForeignKey(blank=True, choices=[('g', 'guitars'), ('d', 'drums'), ('k', 'keyboards'), ('a', 'all')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Analog', verbose_name='Analog'),
        ),
    ]
