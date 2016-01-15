# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 10:09
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accessories', '0003_auto_20160114_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('rate_per_carat', models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoneType',
            fields=[
                ('StoneType_id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.DecimalField(decimal_places=2, max_digits=20)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Stone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accessories.Stone')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stonetype',
            unique_together=set([('StoneType_id', 'Stone')]),
        ),
    ]
