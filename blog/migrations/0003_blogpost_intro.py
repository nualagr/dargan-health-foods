# Generated by Django 3.1.7 on 2021-04-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210419_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]