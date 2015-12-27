# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('cid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('cid', models.CharField(max_length=50)),
                ('in_show', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('eta', models.CharField(max_length=100)),
                ('delivery_date', models.IntegerField(max_length=50)),
                ('net_amout', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together=set([('cid', 'order_id')]),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderForCustomer', to='Customer.OrderDetail'),
        ),
        migrations.AlterUniqueTogether(
            name='customerdetail',
            unique_together=set([('cid', 'order_id')]),
        ),
    ]
