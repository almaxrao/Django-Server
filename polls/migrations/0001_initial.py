# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 17:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(blank=True, null=True)),
                ('user_email', models.TextField(blank=True, null=True)),
                ('user_phone', models.IntegerField(blank=True, null=True)),
                ('user_address', models.TextField(blank=True, null=True)),
                ('user_password_hash', models.TextField(blank=True, null=True)),
                ('user_purchases', models.TextField(blank=True, null=True)),
                ('user_savedlist', models.TextField(blank=True, null=True)),
                ('user_discount_code', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField()),
                ('product_images', models.TextField(blank=True, null=True)),
                ('product_rating', models.FloatField(blank=True, null=True)),
                ('product_price', models.FloatField()),
                ('product_vendor_id', models.IntegerField(blank=True, null=True)),
                ('product_features', models.TextField(blank=True, null=True)),
                ('product_detail', models.TextField(blank=True, null=True)),
                ('product_reviews', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('vendor_it', models.BigAutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.TextField()),
                ('vendor_products_id', models.TextField(blank=True, null=True)),
                ('vendor_reviews', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, max_length=500)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
