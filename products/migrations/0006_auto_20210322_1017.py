# Generated by Django 3.1.7 on 2021-03-22 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210319_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avg_rating',
            new_name='rating',
        ),
    ]