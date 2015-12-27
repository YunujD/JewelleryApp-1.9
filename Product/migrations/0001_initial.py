# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 12:42
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accessories', '0001_initial'),
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loss',
            fields=[
                ('loss_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('loss_type_name', models.CharField(max_length=50)),
                ('loss_in_lal', models.CharField(max_length=100)),
                ('loss_percentage', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_desc', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sharer', to='Category.Category')),
                ('loss_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Loss')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accessories.Material')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='productdetail',
            unique_together=set([('product_id', 'category')]),
        ),
    ]