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
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('category_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('tier_id', models.AutoField(primary_key=True, serialize=False)),
                ('tier_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.Category')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('category_id', 'category_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='tier',
            unique_together=set([('tier_id', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together=set([('sub_category_id', 'category')]),
        ),
    ]