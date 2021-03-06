# Generated by Django 3.1.7 on 2021-03-30 09:12

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_auto_20210322_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('billing_street_address1', models.CharField(max_length=80)),
                ('billing_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('billing_town_or_city', models.CharField(max_length=40)),
                ('billing_county', models.CharField(blank=True, max_length=80, null=True)),
                ('billing_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_country', django_countries.fields.CountryField(max_length=2)),
                ('shipping_street_address1', models.CharField(max_length=80)),
                ('shipping_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('shipping_town_or_city', models.CharField(max_length=40)),
                ('shipping_county', models.CharField(blank=True, max_length=80, null=True)),
                ('shipping_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('shipping_country', django_countries.fields.CountryField(max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_cart', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
