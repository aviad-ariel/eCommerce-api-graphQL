# Generated by Django 3.0.2 on 2020-01-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200118_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='average_products_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]