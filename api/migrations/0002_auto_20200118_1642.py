# Generated by Django 3.0.2 on 2020-01-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='average_products_price',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(related_name='collections', to='api.Product'),
        ),
    ]
