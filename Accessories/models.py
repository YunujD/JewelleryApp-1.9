from __future__ import unicode_literals

import datetime

from django.db import models


class Material(models.Model):
    materialDate = models.CharField(primary_key=True, max_length=15, default=str(datetime.datetime.now().date()))
    goldPrice = models.FloatField(blank=False)
    silverPrice = models.FloatField(blank=False)


# class Stone(models.Model):
# stone_id=models.AutoField(primary_key=True,null=False)
# 	stone_name=models.CharField(max_length=100, unique=True)
# 	price_per_carat=models.IntegerField(max_length=50)

# 	def __unicode__(self):
# 		return self.stone_name

# def StoneType(models.Model):
# 	stone_type_id=models.AutoField(primary_key=True,null=False)
# 	stone_name=models.CharField(max_length=100, unique=True)
# 	price_per_carat=models.IntegerField(max_length=50)
