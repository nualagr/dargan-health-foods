# Generated by Django 3.1.7 on 2021-04-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210429_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='percentage_discount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
